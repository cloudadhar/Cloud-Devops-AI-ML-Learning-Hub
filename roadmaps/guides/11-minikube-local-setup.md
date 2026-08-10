# Minikube - Local Kubernetes Development Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Deploying Applications](#deploying-applications)
5. [DevOps Tools Integration](#devops-tools-integration)
6. [Docker Deployment Pipeline](#docker-deployment-pipeline)
7. [Troubleshooting](#troubleshooting)

---

## 📚 Official Documentation

- **Minikube Official**: https://minikube.sigs.k8s.io/
- **Minikube Documentation**: https://minikube.sigs.k8s.io/docs/
- **Minikube Handbook**: https://minikube.sigs.k8s.io/docs/handbook/
- **Kubernetes Official**: https://kubernetes.io/
- **kubectl CLI Reference**: https://kubernetes.io/docs/reference/kubectl/

---

## Introduction

### What is Minikube?

Minikube is a lightweight Kubernetes implementation that:
- Runs a single-node Kubernetes cluster locally
- Supports multiple operating systems (macOS, Linux, Windows)
- Requires minimal resources (2 CPUs, 2GB RAM)
- Fully compatible with production Kubernetes
- Ideal for learning, development, and testing
- Free and open-source

### When to Use Minikube?

✅ **Use Minikube for:**
- Local development and testing
- Learning Kubernetes
- Testing CI/CD pipelines
- Building applications before cloud deployment
- Testing configurations and deployments
- DevOps tool integration testing

❌ **Don't use Minikube for:**
- Production workloads
- Multi-node clusters
- Heavy load testing
- Production-grade monitoring

---

## Installation

### Prerequisites

**System Requirements:**
- 2 CPUs minimum (4 recommended)
- 2GB RAM minimum (4GB recommended)
- 20GB disk space minimum
- Virtualization support (VT-x/AMD-v)

### macOS Installation

**Option 1: Homebrew (Recommended)**
```bash
# Install Minikube
brew install minikube

# Install kubectl
brew install kubectl

# Verify installation
minikube version
kubectl version --client

# Start cluster
minikube start
```

**Option 2: Direct Download**
```bash
# Download Minikube
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-darwin-amd64
chmod +x minikube-darwin-amd64
sudo mv minikube-darwin-amd64 /usr/local/bin/minikube

# Download kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/darwin/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl
```

### Linux Installation (Ubuntu/Debian)

```bash
# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/kubectl

# Install Minikube
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
chmod +x minikube-linux-amd64
sudo mv minikube-linux-amd64 /usr/local/bin/minikube

# Install Docker (required for container runtime)
sudo apt-get update
sudo apt-get install -y docker.io
sudo usermod -aG docker $USER
newgrp docker

# Start cluster
minikube start --driver=docker
```

### Windows Installation

**Option 1: Chocolatey**
```powershell
choco install minikube kubectl
minikube start
```

**Option 2: Direct Download**
```powershell
# Download and add to PATH
# https://minikube.sigs.k8s.io/docs/start/windows/

# Or using scoop
scoop install minikube kubectl
minikube start
```

### Docker Driver Setup (All Platforms)

```bash
# Install Docker (if not already installed)
# https://docs.docker.com/install/

# Start Minikube with Docker driver
minikube start --driver=docker

# Set Docker as default driver
minikube config set driver docker

# Verify it's running
minikube status
```

---

## Getting Started

### Starting Your First Cluster

```bash
# Start Minikube cluster
minikube start

# This will:
# - Download Minikube ISO (if needed)
# - Start virtual machine
# - Pull Kubernetes components
# - Set up kubectl configuration

# Verify it's running
minikube status
kubectl cluster-info
kubectl get nodes
```

### Basic Commands

```bash
# Check status
minikube status

# Stop cluster
minikube stop

# Start cluster
minikube start

# Delete cluster
minikube delete

# SSH into cluster
minikube ssh

# Open Minikube Dashboard
minikube dashboard

# Get cluster IP
minikube ip

# Open a service in browser
minikube service <service-name>
```

### Using kubectl with Minikube

```bash
# List all resources
kubectl get all

# Get pods
kubectl get pods

# Get services
kubectl get svc

# Get deployments
kubectl get deployments

# Describe a resource
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Execute command in pod
kubectl exec -it <pod-name> -- /bin/bash

# Forward port
kubectl port-forward <pod-name> 8080:80
```

---

## Deploying Applications

### Simple Nginx Deployment

```bash
# Create deployment
kubectl create deployment nginx --image=nginx:latest

# Scale to 3 replicas
kubectl scale deployment nginx --replicas=3

# Expose as service
kubectl expose deployment nginx --type=LoadBalancer --port=80 --target-port=80

# Get service URL
minikube service nginx

# Check pod status
kubectl get pods
kubectl get svc
```

### Using YAML Manifests

**nginx-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-app
  namespace: default
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
        image: nginx:latest
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
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

**Deploy:**
```bash
# Apply manifest
kubectl apply -f nginx-deployment.yaml

# Verify deployment
kubectl get deployments
kubectl get pods
kubectl get svc

# Access service
minikube service nginx-service
```

---

## DevOps Tools Integration

### 1. Building Docker Images Locally

```bash
# Build Docker image for Minikube
docker build -t myapp:1.0 .

# Use Minikube's Docker daemon
eval $(minikube docker-env)

# Now rebuild (image stored in Minikube)
docker build -t myapp:1.0 .

# In deployment, use imagePullPolicy: Never
```

### 2. Local Development Workflow

```bash
# 1. Create source code
mkdir myapp && cd myapp
cat > app.py << 'EOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Minikube!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

# 2. Create Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOF

# 3. Create requirements.txt
echo "Flask==2.0.1" > requirements.txt

# 4. Build image in Minikube
eval $(minikube docker-env)
docker build -t myapp:1.0 .

# 5. Create deployment
kubectl create deployment myapp --image=myapp:1.0
kubectl set env deployment myapp DOCKER_IMAGE_PULL_POLICY=Never

# 6. Expose service
kubectl expose deployment myapp --type=LoadBalancer --port=5000

# 7. Access app
minikube service myapp
```

### 3. SonarQube Integration (Quality Scanning)

```bash
# Deploy SonarQube in Minikube
cat > sonarqube-deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sonarqube
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sonarqube
  template:
    metadata:
      labels:
        app: sonarqube
    spec:
      containers:
      - name: sonarqube
        image: sonarqube:latest
        ports:
        - containerPort: 9000
        env:
        - name: SONARQUBE_JDBC_URL
          value: "jdbc:postgresql://postgres:5432/sonar"
        - name: SONARQUBE_JDBC_USERNAME
          value: "sonar"
        - name: SONARQUBE_JDBC_PASSWORD
          value: "sonar"

---
apiVersion: v1
kind: Service
metadata:
  name: sonarqube
spec:
  selector:
    app: sonarqube
  ports:
  - port: 9000
    targetPort: 9000
  type: LoadBalancer
EOF

kubectl apply -f sonarqube-deployment.yaml

# Access SonarQube
minikube service sonarqube
# Default: admin/admin
```

### 4. Prometheus + Grafana (Monitoring)

```bash
# Add Prometheus Helm chart
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install kube-prometheus-stack
helm install prometheus prometheus-community/kube-prometheus-stack

# Check status
kubectl get pods
kubectl get svc

# Access Prometheus
kubectl port-forward svc/prometheus-kube-prom-prometheus 9090:9090

# Access Grafana (password in secret)
kubectl get secret prometheus-grafana -o jsonpath="{.data.admin-password}" | base64 --decode
kubectl port-forward svc/prometheus-grafana 3000:80
```

### 5. Ingress Controller (Routing)

```bash
# Enable Minikube ingress addon
minikube addons enable ingress

# Create ingress resource
cat > app-ingress.yaml << 'EOF'
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp
            port:
              number: 5000
EOF

kubectl apply -f app-ingress.yaml

# Get Minikube IP
minikube ip

# Add to /etc/hosts
echo "$(minikube ip) myapp.local" >> /etc/hosts

# Access via URL
curl http://myapp.local
```

---

## Docker Deployment Pipeline

### Complete CI/CD with Minikube

**Project Structure:**
```
myapp/
├── src/
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
├── Dockerfile
├── .github/workflows/
│   └── ci-cd.yml
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
└── README.md
```

**1. Dockerfile**
```dockerfile
# Multi-stage build
FROM python:3.9 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY src/ .
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s CMD python -c "import requests; requests.get('http://localhost:5000')"
CMD ["python", "app.py"]
```

**2. GitHub Actions Workflow**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest
      
      - name: Run tests
        run: pytest src/tests/
      
      - name: SonarQube scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v2
      
      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .
      
      - name: Scan image with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: myapp:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
      
      - name: Push to registry
        run: |
          docker tag myapp:${{ github.sha }} myapp:latest
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push myapp:${{ github.sha }}
          docker push myapp:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up kubectl
        uses: azure/setup-kubectl@v1
        with:
          version: 'latest'
      
      - name: Deploy to Minikube
        run: |
          kubectl config use-context minikube
          kubectl set image deployment/myapp myapp=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp
```

**3. Deployment Manifest**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "5000"
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        imagePullPolicy: Never  # For Minikube local development
        ports:
        - containerPort: 5000
          name: http
        env:
        - name: ENVIRONMENT
          value: "production"
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          capabilities:
            drop:
            - ALL

---
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 5000
    protocol: TCP
    name: http
  type: LoadBalancer

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
```

**4. Local Testing Steps**
```bash
# 1. Start Minikube
minikube start --driver=docker

# 2. Build image locally
eval $(minikube docker-env)
docker build -t myapp:latest .

# 3. Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml

# 4. Monitor deployment
kubectl get pods -w
kubectl get svc
kubectl get ingress

# 5. Access application
minikube service myapp-service

# 6. View logs
kubectl logs -f deployment/myapp

# 7. Scale deployment
kubectl scale deployment myapp --replicas=5

# 8. Perform rolling update
kubectl set image deployment/myapp myapp=myapp:v2
kubectl rollout status deployment/myapp

# 9. Rollback if needed
kubectl rollout undo deployment/myapp
```

---

## Advanced Scenarios

### Multi-Container Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-app
spec:
  containers:
  - name: app
    image: myapp:latest
    ports:
    - containerPort: 5000
  - name: sidecar
    image: nginx:latest
    ports:
    - containerPort: 80
  - name: logging
    image: fluent/fluent-bit:latest
```

### StatefulSet for Databases

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgres
spec:
  serviceName: postgres
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:13
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-secret
              key: password
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 5Gi
```

### Helm Chart Deployment

```bash
# Create Helm chart
helm create myapp-chart

# Deploy chart
helm install myapp ./myapp-chart

# Upgrade release
helm upgrade myapp ./myapp-chart

# Rollback
helm rollback myapp

# List releases
helm list
helm history myapp
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **Cluster won't start** | `minikube delete` then `minikube start` |
| **Out of disk space** | `minikube ssh` then `docker system prune` |
| **Pods not starting** | `kubectl describe pod <pod-name>` for details |
| **Service not accessible** | Check: service exists, pod is running, port mapping correct |
| **Image not found** | Use `eval $(minikube docker-env)` before building |
| **Memory issues** | `minikube start --memory=4096` |

### Debug Commands

```bash
# Check cluster health
kubectl cluster-info
kubectl get componentstatuses

# Debug a pod
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous  # Previous container logs

# Get events
kubectl get events --sort-by='.lastTimestamp'

# SSH into Minikube
minikube ssh

# View Minikube logs
minikube logs

# Check resource usage
kubectl top nodes
kubectl top pods
```

---

## ✅ Complete Local DevOps Workflow

```
1. Code → Git
2. Push to GitHub
3. GitHub Actions triggers
4. Tests run (pytest, etc.)
5. SonarQube analyzes code
6. Build Docker image
7. Trivy scans image
8. Deploy to Minikube locally
9. Run smoke tests
10. Monitor with Prometheus/Grafana
11. If successful → Push to registry
12. Deploy to staging/production
```

---

## 📚 Resources

- [Minikube Official](https://minikube.sigs.k8s.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Charts](https://artifacthub.io/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

