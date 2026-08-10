# Kubernetes for Beginners - Container Orchestration

## Table of Contents
1. [Introduction](#introduction)
2. [Core Concepts](#core-concepts)
3. [Installation & Setup](#installation--setup)
4. [Kubernetes Objects](#kubernetes-objects)
5. [Deployments & Scaling](#deployments--scaling)
6. [Services & Networking](#services--networking)
7. [ConfigMaps & Secrets](#configmaps--secrets)
8. [Persistent Storage](#persistent-storage)
9. [Helm Package Manager](#helm-package-manager)
10. [Best Practices](#best-practices)

---

## Introduction

### What is Kubernetes?
Kubernetes (K8s) is a container orchestration platform that:
- Manages containerized applications at scale
- Automatically deploys, scales, and manages containers
- Provides high availability and fault tolerance
- Enables rolling updates and rollbacks
- Self-heals failed containers
- Manages storage, networking, and configuration

**Official Documentation**: https://kubernetes.io/docs

### Architecture

**Control Plane** (Master):
- API Server: Kubernetes API
- etcd: Configuration store
- Scheduler: Assigns pods to nodes
- Controller Manager: Runs controllers

**Worker Nodes**:
- kubelet: Node agent
- Container runtime: Runs containers
- kube-proxy: Network proxy

---

## Core Concepts

### Pod
Smallest unit in Kubernetes, wrapper around container(s):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  namespace: default
spec:
  containers:
  - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
```

### Namespace
Logical cluster subdivision for multi-team environments:

```bash
# Create namespace
kubectl create namespace production

# List namespaces
kubectl get namespaces

# Use namespace
kubectl apply -f deployment.yaml -n production
kubectl get pods -n production
```

### Labels & Selectors
Organize and query objects:

```yaml
metadata:
  labels:
    app: web
    environment: production
    version: v1

selector:
  matchLabels:
    app: web
    environment: production
```

---

## Installation & Setup

### Local Development

**Option 1: Docker Desktop**:
- macOS/Windows: Enable Kubernetes in Docker Desktop settings
- Access at `https://localhost:6443`

**Option 2: Minikube**:

```bash
# Install
brew install minikube

# Start cluster
minikube start --cpus=4 --memory=8192

# Check status
minikube status

# Access dashboard
minikube dashboard

# Get kubeconfig
minikube config view
```

**Option 3: Kind (Kubernetes in Docker)**:

```bash
# Install
brew install kind

# Create cluster
kind create cluster --name dev

# Use cluster
export KUBECONFIG=$(kind get kubeconfig-path --name="dev")
```

### Cloud Providers

**AWS (EKS)**:
```bash
# Create cluster
aws eks create-cluster \
  --name my-cluster \
  --region us-east-1 \
  --kubernetes-network-config serviceIpv4Cidr=10.100.0.0/16

# Get kubeconfig
aws eks update-kubeconfig --name my-cluster --region us-east-1
```

**Azure (AKS)**:
```bash
# Create cluster
az aks create \
  --resource-group mygroup \
  --name mycluster \
  --node-count 3

# Get credentials
az aks get-credentials --resource-group mygroup --name mycluster
```

**GCP (GKE)**:
```bash
# Create cluster
gcloud container clusters create my-cluster \
  --zone us-central1-a \
  --num-nodes 3

# Get credentials
gcloud container clusters get-credentials my-cluster --zone us-central1-a
```

### kubectl Setup

```bash
# Install kubectl
brew install kubectl  # macOS

# Check version
kubectl version

# Check cluster info
kubectl cluster-info

# View nodes
kubectl get nodes
```

---

## Kubernetes Objects

### Deployment
Manages replicated application:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
        version: v1
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
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
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
```

### StatefulSet
For stateful applications (databases, caches):

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: postgresql
spec:
  serviceName: postgresql
  replicas: 1
  selector:
    matchLabels:
      app: postgresql
  template:
    metadata:
      labels:
        app: postgresql
    spec:
      containers:
      - name: postgresql
        image: postgres:14
        ports:
        - containerPort: 5432
        env:
        - name: POSTGRES_DB
          value: myapp
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
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
          storage: 10Gi
```

### DaemonSet
Runs pod on every node (monitoring, logging):

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      containers:
      - name: node-exporter
        image: prom/node-exporter:latest
        ports:
        - containerPort: 9100
```

### Job & CronJob
For batch processing:

```yaml
# Job (one-time)
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-job
spec:
  template:
    spec:
      containers:
      - name: backup
        image: myapp:backup
        command: ["/bin/sh", "-c", "backup-script.sh"]
      restartPolicy: Never
  backoffLimit: 3

---

# CronJob (scheduled)
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "0 2 * * *"  # 2 AM daily
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: myapp:backup
          restartPolicy: OnFailure
```

---

## Deployments & Scaling

### Apply Configuration

```bash
# Apply YAML file
kubectl apply -f deployment.yaml

# Apply all files in directory
kubectl apply -f ./k8s/

# Apply and wait for rollout
kubectl rollout status deployment/nginx-deployment

# View deployment
kubectl get deployments
kubectl describe deployment nginx-deployment

# View pods
kubectl get pods -o wide

# View logs
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>
kubectl logs -f <pod-name>  # Follow logs
```

### Scaling

```bash
# Scale replicas
kubectl scale deployment nginx-deployment --replicas=5

# Autoscaling (requires metrics-server)
kubectl autoscale deployment nginx-deployment \
  --min=3 \
  --max=10 \
  --cpu-percent=80

# View HPA
kubectl get hpa
```

### Rolling Updates

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1         # Max new pods during update
    maxUnavailable: 1   # Max pods down during update
```

```bash
# Update image
kubectl set image deployment/nginx-deployment \
  nginx=nginx:1.22

# Check rollout status
kubectl rollout status deployment/nginx-deployment

# Rollback update
kubectl rollout undo deployment/nginx-deployment

# View rollout history
kubectl rollout history deployment/nginx-deployment
```

---

## Services & Networking

### Service Types

**ClusterIP** (Internal):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

**NodePort** (Expose on nodes):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30000  # 30000-32767
```

**LoadBalancer** (External):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```

### Ingress
HTTP/HTTPS routing:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 5000
  tls:
  - hosts:
    - example.com
    - api.example.com
    secretName: example-tls
```

### Service Discovery

```bash
# Service DNS: <service-name>.<namespace>.svc.cluster.local
# Access from pod:
curl nginx-service.default.svc.cluster.local

# Environment variables:
# <SERVICE_NAME>_SERVICE_HOST
# <SERVICE_NAME>_SERVICE_PORT
```

---

## ConfigMaps & Secrets

### ConfigMap
Non-sensitive configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  app.properties: |
    debug=false
    log_level=info
  database.properties: |
    host=db.example.com
    port=5432
```

Use in deployment:

```yaml
containers:
- name: app
  image: myapp:latest
  env:
  - name: LOG_LEVEL
    valueFrom:
      configMapKeyRef:
        name: app-config
        key: log_level
  volumeMounts:
  - name: config
    mountPath: /etc/config
volumes:
- name: config
  configMap:
    name: app-config
```

### Secret
Sensitive data (passwords, tokens, API keys):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  password: UGFzc3dvcmQxMjMhIQ==  # base64 encoded
  username: YWRtaW4=              # base64 encoded
```

Or use external secrets:

```bash
# Create from file
kubectl create secret generic db-secret \
  --from-literal=password=MyPassword123 \
  --from-literal=username=admin

# Create from file
kubectl create secret generic ssh-key \
  --from-file=id_rsa=~/.ssh/id_rsa
```

Use secret:

```yaml
containers:
- name: app
  image: myapp:latest
  env:
  - name: DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: db-secret
        key: password
```

---

## Persistent Storage

### PersistentVolume (PV)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-storage
spec:
  capacity:
    storage: 10Gi
  accessModes:
  - ReadWriteOnce
  storageClassName: fast
  awsElasticBlockStore:
    volumeID: vol-1234567890abcdef0
    fsType: ext4
```

### PersistentVolumeClaim (PVC)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-pvc
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: fast
  resources:
    requests:
      storage: 5Gi
```

### Use in Pod

```yaml
spec:
  containers:
  - name: app
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: app-pvc
```

---

## Helm Package Manager

### Installation

```bash
# macOS
brew install helm

# Verify
helm version
```

### Using Helm Charts

```bash
# Add Helm repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# Search charts
helm search repo nginx

# Install chart
helm install my-nginx bitnami/nginx \
  --namespace default \
  --values values.yaml

# List releases
helm list

# Upgrade release
helm upgrade my-nginx bitnami/nginx --values values.yaml

# Rollback
helm rollback my-nginx 1

# Uninstall
helm uninstall my-nginx
```

### Create Custom Chart

```bash
# Create chart structure
helm create my-app

# Chart structure:
# my-app/
# ├── Chart.yaml           # Chart metadata
# ├── values.yaml          # Default values
# ├── templates/
# │   ├── deployment.yaml
# │   ├── service.yaml
# │   ├── configmap.yaml
# │   └── ingress.yaml
# └── charts/              # Dependencies

# Package chart
helm package my-app

# Install from local chart
helm install my-release ./my-app \
  --namespace production \
  --values my-app/values.yaml
```

---

## Best Practices

### Resource Management

```yaml
resources:
  requests:          # Guaranteed
    memory: "256Mi"
    cpu: "250m"
  limits:           # Maximum allowed
    memory: "512Mi"
    cpu: "500m"
```

### Health Checks

```yaml
livenessProbe:       # Is pod alive?
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10

readinessProbe:      # Can pod serve traffic?
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
```

### Pod Security

```yaml
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 1000
  containers:
  - name: app
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
```

### Namespace Organization

```bash
# Separate by environment
kubectl create namespace production
kubectl create namespace staging
kubectl create namespace development

# Separate by team
kubectl create namespace team-a
kubectl create namespace team-b
```

### Monitoring & Logging

```bash
# Install metrics-server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.6.1/components.yaml

# View metrics
kubectl top nodes
kubectl top pods

# Install Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus prometheus-community/kube-prometheus-stack
```

---

## Useful Commands

```bash
# Get resources
kubectl get pods
kubectl get services
kubectl get deployments
kubectl get all -n production

# Describe resources
kubectl describe pod <pod-name>
kubectl describe node <node-name>

# Execute commands
kubectl exec -it <pod-name> -- /bin/bash
kubectl exec <pod-name> -- curl localhost:8080

# Port forward
kubectl port-forward service/nginx-service 8080:80

# Delete resources
kubectl delete pod <pod-name>
kubectl delete -f deployment.yaml
kubectl delete namespace production

# Context management
kubectl config get-contexts
kubectl config use-context my-cluster
kubectl config current-context
```

---

## Official Resources

- **Kubernetes Documentation**: https://kubernetes.io/docs
- **API Reference**: https://kubernetes.io/docs/reference/generated/kubernetes-api
- **Helm Charts**: https://artifacthub.io
- **Best Practices**: https://kubernetes.io/docs/concepts/configuration/overview

---

**Last Updated**: August 2026
**Version**: 1.0
