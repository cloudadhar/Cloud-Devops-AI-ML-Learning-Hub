# Nginx - Web Server, Reverse Proxy & Load Balancer

## 📚 Official Documentation
- [Nginx Official](https://nginx.org/) - Official Nginx website
- [Nginx Documentation](https://nginx.org/en/docs/) - Complete documentation
- [Nginx Admin Guide](https://nginx.org/en/docs/admin_guide.html) - Administrator guide
- [Nginx Module Reference](https://nginx.org/en/docs/modules.html) - Module documentation
- [Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/) - Kubernetes Ingress

---

## 🎯 What is Nginx?

Nginx (pronounced "engine-x") is a lightweight, high-performance web server, reverse proxy, and load balancer. It's widely used in production environments.

### Why Learn Nginx?

1. **Web Server**: Serve static files and APIs efficiently
2. **Reverse Proxy**: Route traffic to backend services
3. **Load Balancer**: Distribute traffic across multiple servers
4. **API Gateway**: Basic API routing and rate limiting
5. **Production Standard**: Used by millions of websites
6. **DevOps Essential**: Part of every modern tech stack

### Nginx vs Apache

| Feature | Nginx | Apache |
|---------|-------|--------|
| **Performance** | High (async) | Lower (threaded) |
| **Memory Usage** | Low | High |
| **Concurrency** | Excellent | Good |
| **Configuration** | Simple | Complex |
| **Modules** | Limited built-in | Many modules |
| **Use Case** | Modern apps, APIs | Legacy apps |
| **Learning Curve** | Easy | Moderate |

---

## 📦 Installation Guide

### macOS Installation

#### Option 1: Homebrew (Recommended)
```bash
# Install Nginx
brew install nginx

# Start Nginx
brew services start nginx

# Stop Nginx
brew services stop nginx

# Restart Nginx
brew services restart nginx

# Check status
brew services list
```

#### Option 2: Docker
```bash
# Run latest Nginx
docker run -d -p 80:80 -p 443:443 --name nginx nginx:latest

# Run specific version
docker run -d -p 80:80 --name nginx nginx:1.25

# Access container shell
docker exec -it nginx bash

# Stop and remove
docker stop nginx
docker rm nginx
```

### Linux Installation

#### Ubuntu/Debian
```bash
# Update package manager
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Start Nginx
sudo systemctl start nginx

# Enable on boot
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx

# Verify installation
curl http://localhost
```

#### CentOS/RHEL
```bash
# Install Nginx
sudo yum install -y nginx

# Start Nginx
sudo systemctl start nginx

# Enable on boot
sudo systemctl enable nginx

# Check status
sudo systemctl status nginx
```

#### From Source (Advanced)
```bash
# Download latest version
wget http://nginx.org/download/nginx-1.25.3.tar.gz
tar -xzf nginx-1.25.3.tar.gz
cd nginx-1.25.3

# Configure with modules
./configure \
  --prefix=/etc/nginx \
  --sbin-path=/usr/sbin/nginx \
  --with-http_ssl_module \
  --with-http_gzip_static_module \
  --with-stream

# Build and install
make
sudo make install

# Start Nginx
sudo /usr/sbin/nginx
```

### Windows Installation

#### Option 1: Chocolatey
```powershell
# Install Nginx
choco install nginx

# Start Nginx
nginx

# Stop Nginx
nginx -s stop
```

#### Option 2: Docker (Recommended)
```powershell
# Run Nginx in Docker
docker run -d -p 80:80 --name nginx nginx:latest
```

---

## 🔧 Configuration Basics

### Main Configuration File

**Location**: 
- Linux/macOS: `/etc/nginx/nginx.conf` or `/usr/local/etc/nginx/nginx.conf`
- Docker: `/etc/nginx/nginx.conf`

### Basic nginx.conf Structure

```nginx
# Main context (only one)
user nginx;
worker_processes auto;  # Number of worker processes
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

# Events context (only one)
events {
    worker_connections 1024;  # Max connections per worker
    use epoll;  # Use epoll on Linux for better performance
}

# HTTP context (only one)
http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging format
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;

    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    # Gzip compression
    gzip on;
    gzip_disable "msie6";
    gzip_types text/plain text/css text/xml text/javascript 
               application/json application/javascript application/xml+rss;

    # Include server blocks
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;

    # OR direct server block here
    server {
        listen 80;
        server_name example.com;
        
        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

---

## 🌍 Server Block Configuration

### Simple Web Server (Static Files)

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    # Redirect HTTP to HTTPS (optional)
    # return 301 https://$server_name$request_uri;

    # Root directory for static files
    root /var/www/html;
    
    # Default file to serve
    index index.html index.htm;

    # Serve static files
    location / {
        try_files $uri $uri/ =404;
    }

    # Cache static assets
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg)$ {
        expires 365d;
        add_header Cache-Control "public, immutable";
    }

    # Error pages
    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;

    # Security headers
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
}
```

### Reverse Proxy (Backend Services)

```nginx
upstream backend {
    # Backend servers
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        # Forward requests to backend
        proxy_pass http://backend;
        
        # Preserve original headers
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # WebSocket support
    location /ws {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

### Load Balancer (Round Robin)

```nginx
# Define upstream servers
upstream api_servers {
    # Round robin (default)
    server api1.example.com:8080;
    server api2.example.com:8080;
    server api3.example.com:8080;
    
    # Health check
    # server api4.example.com:8080 max_fails=3 fail_timeout=30s;
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://api_servers;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Load Balancing Methods

```nginx
# Round Robin (default)
upstream backend_rr {
    server server1.example.com;
    server server2.example.com;
}

# Least Connections
upstream backend_lc {
    least_conn;
    server server1.example.com;
    server server2.example.com;
}

# IP Hash (sticky sessions)
upstream backend_ip {
    ip_hash;
    server server1.example.com;
    server server2.example.com;
}

# Weight-based
upstream backend_weight {
    server server1.example.com weight=5;
    server server2.example.com weight=3;
    server server3.example.com weight=1;
}

# Random
upstream backend_random {
    random;
    server server1.example.com;
    server server2.example.com;
}
```

---

## 🔒 HTTPS/SSL Configuration

### Self-Signed Certificate (Testing)

```bash
# Generate private key and certificate
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/private.key \
  -out /etc/nginx/ssl/certificate.crt

# Generate with non-interactive mode
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/private.key \
  -out /etc/nginx/ssl/certificate.crt \
  -subj "/C=US/ST=State/L=City/O=Organization/CN=example.com"
```

### HTTPS Server Block

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    # SSL certificates
    ssl_certificate /etc/nginx/ssl/certificate.crt;
    ssl_certificate_key /etc/nginx/ssl/private.key;

    # SSL protocols and ciphers
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Performance
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    # Root and index
    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

# Redirect HTTP to HTTPS
server {
    listen 80;
    server_name example.com;
    return 301 https://$server_name$request_uri;
}
```

### Let's Encrypt with Certbot

```bash
# Install Certbot
sudo apt-get install -y certbot python3-certbot-nginx

# Generate certificate
sudo certbot certonly --nginx -d example.com -d www.example.com

# Nginx configuration with Let's Encrypt
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    root /var/www/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

# Auto-renew certificates
sudo certbot renew --dry-run
```

---

## 📋 Essential Commands

```bash
# Check Nginx version
nginx -v

# Check configuration syntax
nginx -t

# View full configuration details
nginx -T

# Start Nginx
sudo systemctl start nginx
# OR on macOS
sudo nginx

# Stop Nginx
sudo systemctl stop nginx
# OR
sudo nginx -s stop

# Reload configuration (no downtime)
sudo nginx -s reload
# OR
sudo systemctl reload nginx

# Restart Nginx
sudo systemctl restart nginx

# View process
ps aux | grep nginx

# Check listening ports
sudo netstat -tlnp | grep nginx
# OR (newer systems)
sudo ss -tlnp | grep nginx

# View access logs
sudo tail -f /var/log/nginx/access.log

# View error logs
sudo tail -f /var/log/nginx/error.log

# Check open file limits
ulimit -n

# Increase file descriptors (if needed)
sudo nano /etc/security/limits.conf
# Add: nginx soft nofile 65535
# Add: nginx hard nofile 65535
```

---

## 🎮 Hands-On Examples

### Example 1: Simple Static Website

```nginx
server {
    listen 80;
    server_name myapp.local;

    root /home/user/myapp/public;
    index index.html;

    location / {
        # Try file first, then directory, then 404
        try_files $uri $uri/ =404;
    }

    # Cache busting for assets
    location ~* \.(js|css|png|jpg|gif|ico|woff|woff2)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

**Create test files**:
```bash
mkdir -p ~/myapp/public
cat > ~/myapp/public/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>My App</title></head>
<body><h1>Hello from Nginx!</h1></body>
</html>
EOF

# Test in browser: http://myapp.local
```

### Example 2: Docker Application

```nginx
upstream nodejs_backend {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}

server {
    listen 80;
    server_name app.example.com;

    location / {
        proxy_pass http://nodejs_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }

    location /static/ {
        alias /var/www/static/;
        expires 30d;
    }
}
```

### Example 3: Kubernetes Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: frontend
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: backend
            port:
              number: 3000
  tls:
  - hosts:
    - example.com
    secretName: example-com-tls
```

### Example 4: Rate Limiting

```nginx
# Define rate limit zone
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=login_limit:10m rate=5r/m;

server {
    listen 80;
    server_name api.example.com;

    # Apply rate limit to API
    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
        proxy_pass http://backend;
    }

    # Strict rate limit for login
    location /api/login {
        limit_req zone=login_limit burst=5 nodelay;
        proxy_pass http://backend;
    }
}
```

---

## 🔐 Security Best Practices

### 1. Hide Nginx Version
```nginx
server_tokens off;  # Add to http {} block
```

### 2. Security Headers
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self';" always;
```

### 3. Limit Request Size
```nginx
client_max_body_size 10M;  # Prevent large uploads
```

### 4. Disable Unnecessary Methods
```nginx
location / {
    limit_except GET POST HEAD {
        deny all;
    }
}
```

### 5. Rate Limiting (DDoS Protection)
```nginx
limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=addr:10m;

server {
    limit_req zone=general burst=20 nodelay;
    limit_conn addr 10;
}
```

---

## 📊 Performance Tuning

### 1. Worker Process Optimization
```nginx
worker_processes auto;  # Auto-detect CPU cores
worker_connections 2048;  # Increase for high traffic
```

### 2. Enable Gzip Compression
```nginx
gzip on;
gzip_vary on;
gzip_comp_level 6;
gzip_types text/plain text/css text/xml text/javascript 
           application/json application/javascript application/xml+rss 
           application/rss+xml application/atom+xml image/svg+xml 
           text/x-js text/x-component text/x-cross-domain-policy;
```

### 3. Enable Caching
```nginx
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m;

location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 302 10m;
    proxy_cache_valid 404 1m;
    add_header X-Cache-Status $upstream_cache_status;
}
```

### 4. Connection Pooling
```nginx
upstream backend {
    keepalive 32;
    server backend1.example.com;
    server backend2.example.com;
}

server {
    location / {
        proxy_pass http://backend;
        proxy_http_version 1.1;
        proxy_set_header Connection "";
    }
}
```

---

## 🐛 Troubleshooting

### Check Configuration Errors
```bash
sudo nginx -t
sudo nginx -T  # Show full config
```

### View Logs
```bash
# Real-time access logs
sudo tail -f /var/log/nginx/access.log

# Real-time error logs
sudo tail -f /var/log/nginx/error.log

# Search error logs
sudo grep "error" /var/log/nginx/error.log
```

### Common Issues

| Issue | Solution |
|-------|----------|
| Port 80 already in use | `sudo lsof -i :80` and stop conflicting service |
| Permission denied | Use `sudo` or ensure nginx user has permissions |
| 502 Bad Gateway | Check upstream server status: `curl http://backend:8080` |
| High memory usage | Reduce `worker_connections` or `worker_processes` |
| Slow response | Enable gzip, caching, and check upstream server performance |
| SSL certificate issues | Verify certificate path and syntax with `nginx -t` |

---

## 🚀 Deployment Examples

### Docker Compose
```yaml
version: '3.8'
services:
  nginx:
    image: nginx:1.25
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./public:/var/www/html:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - backend

  backend:
    image: myapp:latest
    ports:
      - "3000"
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
  type: LoadBalancer
```

---

## 📚 Learning Path

### Beginner (Week 1-2)
1. Install Nginx locally
2. Serve static files
3. Understand basic configuration
4. Practice basic proxy

### Intermediate (Week 3-4)
1. Reverse proxy to multiple backends
2. Load balancing techniques
3. HTTPS/SSL setup
4. Logging and monitoring

### Advanced (Week 5-6)
1. Performance optimization
2. Security hardening
3. Rate limiting and DDoS protection
4. Kubernetes Ingress Controller
5. Advanced caching strategies

---

## 🎯 Interview Questions

1. **What is the difference between Nginx and Apache?**
   - Answer: Nginx uses async I/O model for better performance, lower memory, ideal for modern high-concurrency applications. Apache uses threaded model, suitable for legacy applications.

2. **Explain reverse proxy.**
   - Answer: A reverse proxy forwards client requests to backend servers and returns responses to clients. It hides backend server details, enables load balancing, and improves security.

3. **How do you enable HTTPS in Nginx?**
   - Answer: Configure SSL certificate and key paths in `server` block, set `listen 443 ssl`, specify `ssl_certificate` and `ssl_certificate_key` paths.

4. **What's the purpose of upstream blocks?**
   - Answer: Define backend server groups for load balancing. Multiple backends can be listed with different load balancing methods (round-robin, least-conn, ip-hash, etc.).

5. **How do you reload Nginx without downtime?**
   - Answer: Use `nginx -s reload` or `systemctl reload nginx` to gracefully reload configuration and existing connections.

---

## 🔗 Validation References

- [Nginx Official Documentation](https://nginx.org/en/docs/)
- [Nginx Admin Guide](https://nginx.org/en/docs/admin_guide.html)
- [Nginx Module Reference](https://nginx.org/en/docs/modules.html)
- [Kubernetes Ingress Nginx](https://kubernetes.github.io/ingress-nginx/)
- [Nginx Security Best Practices](https://nginx.org/en/docs/http/ngx_http_core_module.html)

