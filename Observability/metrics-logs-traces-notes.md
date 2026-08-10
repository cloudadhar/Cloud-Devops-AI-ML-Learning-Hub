# Metrics, Logs, and Traces Notes

## 📚 Official Documentation

### Metrics & Monitoring
- **Prometheus Official**: https://prometheus.io/
- **Prometheus Docs**: https://prometheus.io/docs/
- **Prometheus Installation**: https://prometheus.io/download/
- **Prometheus Configuration**: https://prometheus.io/docs/prometheus/latest/configuration/configuration/
- **PromQL Guide**: https://prometheus.io/docs/prometheus/latest/querying/basics/

### Logs & Aggregation
- **ELK Stack**: https://www.elastic.co/guide/index.html
- **Grafana Loki**: https://grafana.com/docs/loki/latest/
- **OpenSearch**: https://opensearch.org/docs/

### Tracing & APM
- **Jaeger**: https://www.jaegertracing.io/docs/
- **Grafana Tempo**: https://grafana.com/docs/tempo/latest/
- **OpenTelemetry**: https://opentelemetry.io/docs/

### Dashboards & Visualization
- **Grafana**: https://grafana.com/docs/
- **Grafana Cloud**: https://grafana.com/products/cloud/

---

## 📊 Metrics

### What are Metrics?
Metrics are numeric measurements over time collected from systems and applications.

**Examples:**
- CPU usage (%)
- Memory usage (bytes)
- Request count (total)
- Error rate (%)
- Latency (milliseconds)
- Queue depth (items)
- Disk I/O (bytes/sec)
- Network throughput (packets/sec)

### Metric Types

**Counter** - Only increases
```
# Requests processed
http_requests_total{method="GET"} 1024
```

**Gauge** - Can go up or down
```
# Current memory usage
memory_usage_bytes{instance="server1"} 2147483648
```

**Histogram** - Distribution over buckets
```
# Request latency distribution
http_request_duration_seconds_bucket{le="0.1"}
http_request_duration_seconds_bucket{le="0.5"}
http_request_duration_seconds_bucket{le="1.0"}
```

**Summary** - Percentiles
```
# Query duration percentiles
query_duration_seconds{quantile="0.5"}  # p50
query_duration_seconds{quantile="0.99"} # p99
```

### Time Series
- Metric name + labels = unique time series
- Example: `http_requests_total{method="GET", endpoint="/api/users"}`

---

## 🔧 Prometheus - Complete Setup Guide

### What is Prometheus?

Prometheus is a time-series database and monitoring system:
- **Pull-based**: Scrapes metrics from applications
- **Time-series database**: Stores metric data with timestamps
- **Query language**: PromQL for analyzing metrics
- **Alerting**: Can trigger alerts on conditions
- **Multi-dimensional**: Labels for querying and filtering

### Installation

#### Option 1: Docker (Recommended for Development)

```bash
# Create prometheus config
mkdir -p /tmp/prometheus
cat > /tmp/prometheus/prometheus.yml << 'EOF'
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
EOF

# Run Prometheus
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v /tmp/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:latest

# Access at http://localhost:9090
```

#### Option 2: Docker Compose

```yaml
version: '3.9'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - ./alerts.yml:/etc/prometheus/alerts.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
    networks:
      - monitoring

  node_exporter:
    image: prom/node-exporter:latest
    container_name: node_exporter
    ports:
      - "9100:9100"
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring
    depends_on:
      - prometheus

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
    driver: bridge
```

#### Option 3: Linux Installation (Ubuntu/Debian)

```bash
# Download Prometheus
cd /tmp
wget https://github.com/prometheus/prometheus/releases/download/v2.45.0/prometheus-2.45.0.linux-amd64.tar.gz

# Extract
tar xvfz prometheus-2.45.0.linux-amd64.tar.gz
cd prometheus-2.45.0.linux-amd64

# Create systemd service
sudo tee /etc/systemd/system/prometheus.service > /dev/null << 'EOF'
[Unit]
Description=Prometheus
After=network.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus

[Install]
WantedBy=multi-user.target
EOF

# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus

# Check status
sudo systemctl status prometheus
```

#### Option 4: macOS (Homebrew)

```bash
# Install
brew install prometheus

# Create config directory
mkdir -p $(brew --prefix)/etc/prometheus

# Create config file (see below)
# Edit: $(brew --prefix)/etc/prometheus/prometheus.yml

# Start service
brew services start prometheus

# Access at http://localhost:9090
```

---

### Configuration

#### Basic prometheus.yml

```yaml
# Global settings
global:
  scrape_interval: 15s           # Scrape every 15 seconds
  evaluation_interval: 15s       # Evaluate rules every 15 seconds
  external_labels:
    monitor: 'my-cluster'

# Alerting configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['localhost:9093']

# Load rules
rule_files:
  - 'alerts.yml'
  - 'recording_rules.yml'

# Scrape configurations
scrape_configs:
  # Prometheus itself
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node exporter (system metrics)
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # Your application
  - job_name: 'myapp'
    static_configs:
      - targets: ['localhost:8000']
    metrics_path: '/metrics'
    scrape_interval: 10s

  # Docker containers
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['localhost:8080']
```

#### Advanced Configuration

**Service Discovery (AWS)**
```yaml
scrape_configs:
  - job_name: 'ec2'
    ec2_sd_configs:
      - region: us-east-1
        port: 9100
```

**Kubernetes Service Discovery**
```yaml
scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
```

---

### Configuring Metrics in Applications

#### Python (with prometheus-client)

```python
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from flask import Flask

app = Flask(__name__)

# Define metrics
request_count = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
request_duration = Histogram('http_request_duration_seconds', 'HTTP request duration')
active_connections = Gauge('active_connections', 'Number of active connections')

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    # Record request count
    request_count.labels(method=request.method, endpoint=request.path).inc()
    
    # Record duration
    duration = time.time() - request.start_time
    request_duration.observe(duration)
    
    return response

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/api/users')
def get_users():
    active_connections.set(len(get_active_users()))
    return {'users': []}
```

#### Node.js (with prom-client)

```javascript
const express = require('express');
const promClient = require('prom-client');

const app = express();

// Create metrics
const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
});

const httpRequestTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code'],
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration
      .labels(req.method, req.route.path, res.statusCode)
      .observe(duration);
    httpRequestTotal
      .labels(req.method, req.route.path, res.statusCode)
      .inc();
  });
  
  next();
});

// Expose metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', promClient.register.contentType);
  res.end(await promClient.register.metrics());
});
```

#### Java (with Micrometer)

```java
@RestController
public class UserController {
  private final MeterRegistry meterRegistry;
  
  public UserController(MeterRegistry meterRegistry) {
    this.meterRegistry = meterRegistry;
  }
  
  @GetMapping("/users")
  public List<User> getUsers() {
    // Counter
    meterRegistry.counter("users.fetched").increment();
    
    // Gauge
    meterRegistry.gauge("active.users", activeUsers.size());
    
    // Timer
    Timer timer = meterRegistry.timer("user.fetch.duration");
    return timer.recordCallable(() -> userService.getUsers());
  }
}

// In application.yml
management:
  endpoints:
    web:
      exposure:
        include: prometheus
  metrics:
    export:
      prometheus:
        enabled: true
```

---

### PromQL - Querying Metrics

#### Basic Queries

```promql
# Get current value
http_requests_total

# Get specific label
http_requests_total{method="GET"}

# Multiple labels
http_requests_total{method="GET", endpoint="/api"}
```

#### Rate & Increase

```promql
# Requests per second (5-minute average)
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status="500"}[5m]) / rate(http_requests_total[5m])

# Total requests in last hour
increase(http_requests_total[1h])
```

#### Aggregation

```promql
# Sum across all instances
sum(http_requests_total)

# Average
avg(node_cpu_seconds_total)

# Per instance
sum by(instance) (http_requests_total)

# Top 5
topk(5, http_requests_total)
```

#### Functions

```promql
# Moving average
avg_over_time(cpu_usage[5m])

# Predictions
predict_linear(cpu_usage[1h], 3600)

# Histograms
histogram_quantile(0.95, http_request_duration_seconds)
```

---

## 📝 Logs

### What are Logs?
Logs are event records from applications and systems.

**Examples:**
- Request logs (timestamp, method, endpoint, status)
- Error logs (stack traces, error messages)
- Audit logs (who did what when)
- Access logs (Nginx, Kong, API Gateway)
- Application logs (debug, info, warning, error)

---

## 🔍 Traces

### What are Traces?
Traces show the complete request flow across services in a distributed system.

**Useful for:**
- Microservices debugging
- Identifying performance bottlenecks
- API gateway monitoring
- Slow request analysis
- Root cause analysis

---

## ✨ Golden Signals

Key metrics to monitor:
- **Latency**: How slow is the service?
- **Traffic**: How many requests?
- **Errors**: What's the error rate?
- **Saturation**: How full are resources?

---

## 📋 Practice Exercises

1. **Install and configure Prometheus**
   - Set up Prometheus Docker container
   - Configure 3 scrape targets
   - Access Prometheus UI

2. **Add application metrics**
   - Instrument Python/Node.js/Java app
   - Expose /metrics endpoint
   - Verify metrics appear in Prometheus

3. **Build Grafana dashboard**
   - Add Prometheus as datasource
   - Create dashboard with 5 panels
   - Add variables for filtering

4. **Set up alerting**
   - Create alert rule for high error rate
   - Configure AlertManager
   - Test alert triggering

5. **Write postmortem**
   - Simulate a failure scenario
   - Use metrics to diagnose issue
   - Document findings and remediation
