# Prometheus & Grafana - Monitoring & Observability

## Table of Contents
1. [Introduction](#introduction)
2. [Prometheus Installation](#prometheus-installation)
3. [Prometheus Configuration](#prometheus-configuration)
4. [Grafana Installation](#grafana-installation)
5. [Dashboards & Alerts](#dashboards--alerts)
6. [Grafana Cloud](#grafana-cloud)
7. [Best Practices](#best-practices)

---

## Introduction

### What is Prometheus?
Prometheus is a time-series database and monitoring system:
- Collects metrics from applications and infrastructure
- Stores metrics with timestamps
- Query language (PromQL) for analysis
- Alert generation
- Pull-based (scrapes metrics)
- Multi-dimensional labels

**Official Documentation**: https://prometheus.io/docs

### What is Grafana?
Grafana is a visualization and alerting platform:
- Visualizes Prometheus metrics
- Creates interactive dashboards
- Multi-datasource support
- Alert management
- User access control
- Community and enterprise versions

**Official Documentation**: https://grafana.com/docs

**Getting Started Guides:**
- [Install Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)
- [Get started with Grafana and Prometheus](https://grafana.com/docs/grafana/latest/fundamentals/getting-started/first-dashboards/get-started-grafana-prometheus/)

### Metric Types
- **Counter**: Only increases (page views, errors)
- **Gauge**: Can go up or down (memory usage, CPU)
- **Histogram**: Distribution over buckets (request latency)
- **Summary**: Percentiles (query duration)

---

## Prometheus Installation

### Option 1: Docker (Development)

```bash
# Run Prometheus
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus:latest \
  --config.file=/etc/prometheus/prometheus.yml

# Access at http://localhost:9090
```

### Option 2: Docker Compose

Create `docker-compose.yml`:

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
      - '--web.console.libraries=/usr/share/prometheus/console_libraries'
      - '--web.console.templates=/usr/share/prometheus/consoles'
    restart: unless-stopped
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin
      GF_USERS_ALLOW_SIGN_UP: false
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana-provisioning:/etc/grafana/provisioning
    restart: unless-stopped
    networks:
      - monitoring
    depends_on:
      - prometheus

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    ports:
      - "9100:9100"
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    restart: unless-stopped
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
    driver: bridge
```

```bash
docker-compose up -d
# Prometheus: http://localhost:9090
# Grafana: http://localhost:3000
```

### Option 3: Standalone Installation

```bash
# macOS
brew install prometheus

# Ubuntu/Debian
wget https://github.com/prometheus/prometheus/releases/download/v2.46.0/prometheus-2.46.0.linux-amd64.tar.gz
tar -xzf prometheus-2.46.0.linux-amd64.tar.gz
cd prometheus-2.46.0.linux-amd64
./prometheus --config.file=prometheus.yml
```

---

## Prometheus Configuration

### Create prometheus.yml

```yaml
# prometheus.yml
global:
  scrape_interval: 15s  # Default scrape interval
  evaluation_interval: 15s  # Alert evaluation interval
  external_labels:
    monitor: 'my-monitor'
    environment: 'production'

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - localhost:9093

# Load rules
rule_files:
  - 'alerts.yml'
  - 'recording-rules.yml'

# Scrape configurations
scrape_configs:
  # Prometheus itself
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Node Exporter (system metrics)
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # Application metrics
  - job_name: 'app'
    static_configs:
      - targets: ['localhost:8080']
    scrape_interval: 5s
    metrics_path: '/metrics'

  # Kubernetes (if applicable)
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
      - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token

  # Docker containers
  - job_name: 'docker'
    static_configs:
      - targets: ['localhost:9323']

  # Service discovery (Consul)
  - job_name: 'consul-services'
    consul_sd_configs:
      - server: 'localhost:8500'
```

### Exporters (Data Collectors)

**Node Exporter** (System metrics):
```bash
docker run -d \
  --name node-exporter \
  -p 9100:9100 \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /:/rootfs:ro \
  prom/node-exporter:latest
```

**Docker Metrics**:
```bash
docker run -d \
  --name cadvisor \
  -p 8080:8080 \
  -v /:/rootfs:ro \
  -v /var/run:/var/run:ro \
  -v /sys:/sys:ro \
  -v /var/lib/docker/:/var/lib/docker:ro \
  gcr.io/cadvisor/cadvisor:latest
```

**Application Metrics** (Instrumentation):

Node.js:
```javascript
const prometheus = require('prom-client');

// Create metrics
const httpRequestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code'],
  buckets: [0.1, 0.5, 1, 2, 5]
});

const httpRequestTotal = new prometheus.Counter({
  name: 'http_requests_total',
  help: 'Total HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

// Middleware
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration.observe(
      { method: req.method, route: req.route?.path, status_code: res.statusCode },
      duration
    );
    httpRequestTotal.inc({
      method: req.method,
      route: req.route?.path,
      status_code: res.statusCode
    });
  });
  next();
});

// Expose metrics
app.get('/metrics', (req, res) => {
  res.set('Content-Type', prometheus.register.contentType);
  res.end(prometheus.register.metrics());
});
```

Python:
```python
from prometheus_client import Counter, Histogram, start_http_server
import time

# Create metrics
http_requests_total = Counter(
    'http_requests_total', 'Total HTTP requests',
    ['method', 'endpoint', 'status']
)
http_request_duration = Histogram(
    'http_request_duration_seconds', 'HTTP request duration',
    ['method', 'endpoint']
)

# Middleware
def prometheus_middleware(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = f(*args, **kwargs)
            return result
        finally:
            duration = time.time() - start
            http_request_duration.labels(method='GET', endpoint='/api').observe(duration)
            http_requests_total.labels(method='GET', endpoint='/api', status=200).inc()
    return wrapper

# Start metrics server
start_http_server(8000)
```

---

## Grafana Installation

### Option 1: Docker

```bash
docker run -d \
  --name grafana \
  -p 3000:3000 \
  -e GF_SECURITY_ADMIN_PASSWORD=admin \
  grafana/grafana:latest

# Access at http://localhost:3000
# Default: admin/admin
```

### Option 2: Docker Compose (with Prometheus)

See previous section - included in docker-compose.yml

### Option 3: Standalone

```bash
# macOS
brew install grafana

# Ubuntu/Debian
sudo apt-get install -y grafana-server

# Start
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

---

## Dashboards & Alerts

### Add Prometheus Datasource

1. Go to http://localhost:3000
2. Login (admin/admin)
3. Go to Configuration → Data sources
4. Click "Add data source"
5. Select "Prometheus"
6. URL: `http://prometheus:9090`
7. Save

### Create Dashboard

**Option 1: From scratch**:
1. Click "+" → Dashboard
2. Add panel
3. Select Prometheus
4. Write PromQL query:

```promql
# CPU usage
rate(node_cpu_seconds_total{mode="idle"}[5m]) * 100

# Memory usage
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100

# Request rate
rate(http_requests_total[5m])

# Error rate
rate(http_requests_total{status=~"5.."}[5m])

# Response time (95th percentile)
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
```

**Option 2: Import community dashboards**:
1. Go to Dashboard → Import
2. Enter ID from https://grafana.com/grafana/dashboards
3. Select Prometheus datasource
4. Import

Popular dashboards:
- Node Exporter: 1860
- Prometheus: 3662
- Docker: 12114

### Create Alerts

Create `alerts.yml`:

```yaml
groups:
  - name: system
    interval: 30s
    rules:
      # High CPU usage
      - alert: HighCPUUsage
        expr: (100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage on {{ $labels.instance }}"
          description: "CPU usage is {{ $value }}%"

      # High memory usage
      - alert: HighMemoryUsage
        expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 90
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High memory usage on {{ $labels.instance }}"
          description: "Memory usage is {{ $value }}%"

      # High error rate
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.1
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "High error rate"
          description: "Error rate is {{ $value }} errors/sec"

      # High latency
      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High latency detected"
          description: "P95 latency is {{ $value }}s"
```

### Setup AlertManager

Create `alertmanager.yml`:

```yaml
global:
  resolve_timeout: 5m
  slack_api_url: 'YOUR_SLACK_WEBHOOK_URL'

route:
  receiver: 'default'
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 10s
  group_interval: 10s
  repeat_interval: 12h
  routes:
    - match:
        severity: critical
      receiver: critical
      continue: true

receivers:
  - name: 'default'
    slack_configs:
      - channel: '#alerts'
        title: 'Alert: {{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'

  - name: 'critical'
    slack_configs:
      - channel: '#critical-alerts'
        title: 'CRITICAL: {{ .GroupLabels.alertname }}'
        text: '{{ range .Alerts }}{{ .Annotations.description }}{{ end }}'
    pagerduty_configs:
      - service_key: 'YOUR_PAGERDUTY_KEY'
```

Run AlertManager:

```bash
docker run -d \
  --name alertmanager \
  -p 9093:9093 \
  -v $(pwd)/alertmanager.yml:/etc/alertmanager/alertmanager.yml \
  prom/alertmanager:latest
```

---

## Grafana Cloud

### What is Grafana Cloud?
Managed Grafana hosting with:
- Pre-configured Prometheus
- Loki for logs
- Tempo for traces
- Email alerts
- Integration with on-prem systems

### Setup Grafana Cloud

1. Sign up at https://grafana.com/auth/sign-up
2. Create stack
3. Get API token
4. Configure agent on servers:

```bash
# Download Grafana Agent
wget https://github.com/grafana/agent/releases/download/v0.35.0/grafana-agent-linux-amd64.zip
unzip grafana-agent-linux-amd64.zip

# Create config
cat > agent-config.yaml <<EOF
integrations:
  prometheus_remote_write:
    - url: YOUR_GRAFANA_CLOUD_PROMETHEUS_URL
      basic_auth:
        username: YOUR_USERNAME
        password: YOUR_API_TOKEN

  node_exporter:
    enabled: true
EOF

# Run agent
./grafana-agent -config.file=agent-config.yaml
```

---

## Best Practices

### Metric Naming
- ✅ `<namespace>_<subsystem>_<name>_<unit>`
- ✅ `http_request_duration_seconds`
- ✅ `database_connections_active`
- ✅ `cache_hits_total`

### Cardinality Control
- ⚠️ Avoid high cardinality labels (too many unique values)
- ✅ Use fixed labels only
- ✅ Limit user IDs, request IDs in labels

### Dashboard Best Practices
- ✅ Clear titles and descriptions
- ✅ Group related metrics
- ✅ Use appropriate visualization types
- ✅ Set reasonable time ranges
- ✅ Template dashboards for reuse

### Alert Best Practices
- ✅ Alert on symptoms, not causes
- ✅ Avoid alert fatigue (tune thresholds)
- ✅ Clear alert messages with runbooks
- ✅ Add severity levels
- ✅ Test alert flows

### Performance & Storage
- ✅ Adjust scrape intervals appropriately
- ✅ Set data retention (default 15 days)
- ✅ Use remote storage (S3, GCS) for long-term
- ✅ Monitor Prometheus performance

---

## PromQL Examples

```promql
# Rate of growth
rate(metric_name[5m])

# Average CPU usage
avg(node_cpu_seconds_total) by (instance)

# Percentiles
histogram_quantile(0.95, metric_name)

# Filtering
metric{status="200", method="GET"}

# Aggregation
sum by (instance) (metric_name)
count by (status) (http_requests_total)

# Time shift
metric_name offset 1h

# Threshold checking
metric_name > 100

# Comparison
metric_1 / metric_2
```

---

## Official Resources

- **Prometheus Docs**: https://prometheus.io/docs
- **Prometheus Functions**: https://prometheus.io/docs/prometheus/latest/querying/functions
- **Grafana Docs**: https://grafana.com/docs
- **Grafana Cloud**: https://grafana.com/products/cloud

---

**Last Updated**: August 2026
**Version**: 1.0
