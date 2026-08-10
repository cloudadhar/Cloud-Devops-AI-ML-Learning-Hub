# Kubernetes Notes - Container Orchestration & Local Development

## 📚 Official Documentation

- **Kubernetes Official**: https://kubernetes.io/
- **Kubernetes Docs**: https://kubernetes.io/docs/
- **kubectl Reference**: https://kubernetes.io/docs/reference/kubectl/
- **API Reference**: https://kubernetes.io/docs/reference/generated/kubernetes-api/latest/
- **Minikube Official**: https://minikube.sigs.k8s.io/
- **Minikube Documentation**: https://minikube.sigs.k8s.io/docs/

---

## 🚀 Kubernetes Alternatives for Local Development

### Minikube (Recommended for Beginners)
- **Purpose**: Single-node local Kubernetes cluster
- **Resources**: Minimal (2GB RAM, 2 CPUs)
- **Setup Time**: ~5 minutes
- **Best For**: Learning, development, testing
- **Website**: https://minikube.sigs.k8s.io/

### Docker Desktop Kubernetes
- **Purpose**: Built-in Kubernetes in Docker Desktop
- **Resources**: Minimal
- **Setup Time**: ~1 minute (if Docker Desktop already installed)
- **Best For**: Quick local testing
- **How to Enable**: Docker Desktop → Preferences → Kubernetes → Enable Kubernetes

### Kind (Kubernetes in Docker)
- **Purpose**: Multi-node cluster in Docker containers
- **Resources**: Low to moderate
- **Setup Time**: ~5 minutes
- **Best For**: Testing multi-node scenarios
- **Website**: https://kind.sigs.k8s.io/

### Kubeadm
- **Purpose**: Production-like cluster setup
- **Resources**: Moderate to high
- **Setup Time**: ~30 minutes
- **Best For**: Learning production setup
- **Website**: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/

### k3s (Lightweight Kubernetes)
- **Purpose**: Minimal Kubernetes distribution
- **Resources**: Very low (~512MB RAM)
- **Setup Time**: ~2 minutes
- **Best For**: Edge computing, IoT
- **Website**: https://k3s.io/

---

## Minikube Quick Start

### Install Minikube

**macOS:**
```bash
brew install minikube kubectl
minikube start
```

**Linux:**
```bash
curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start --driver=docker
```

**Windows:**
```powershell
choco install minikube kubectl
minikube start
```

### Basic Commands

```bash
minikube start              # Start cluster
minikube stop               # Stop cluster
minikube delete             # Delete cluster
minikube status             # Check status
minikube dashboard          # Open web dashboard
minikube service <name>     # Open service in browser
minikube ip                 # Get cluster IP
```

---

## 🎯 Core Objects

| Object | Purpose | Example |
| --- | --- | --- |
| **Pod** | Smallest deployable unit | Single container wrapper |
| **Deployment** | Manages replicas and rolling updates | 3 nginx replicas |
| **Service** | Stable network access to pods | Load balancer for pods |
| **Ingress** | HTTP routing from outside cluster | Route to multiple services |
| **ConfigMap** | Non-secret configuration | Database host, port |
| **Secret** | Sensitive configuration | Passwords, API keys |
| **Namespace** | Logical grouping | Separate prod and dev |
| **PersistentVolumeClaim** | Storage request | Database volume |
| **StatefulSet** | For stateful applications | Databases, caches |
| **DaemonSet** | Runs on all nodes | Logging, monitoring agents |

---

## Basic Debug Commands

```bash
# Check cluster and nodes
kubectl cluster-info
kubectl get nodes

# Pod management
kubectl get pods                          # List pods
kubectl get pods -n <namespace>           # List pods in namespace
kubectl describe pod <pod-name>           # Pod details
kubectl logs <pod-name>                   # View logs
kubectl logs <pod-name> --previous        # Previous container logs
kubectl exec -it <pod-name> -- /bin/bash  # SSH into pod

# Service and networking
kubectl get svc                           # List services
kubectl get ingress                       # List ingresses
kubectl port-forward pod/<name> 8080:80   # Forward port

# Events and troubleshooting
kubectl get events --sort-by='.lastTimestamp'  # Recent events
kubectl top nodes                              # Resource usage
kubectl top pods                               # Pod resource usage

# Deployment management
kubectl get deployments                   # List deployments
kubectl scale deployment <name> --replicas=3  # Scale replicas
kubectl set image deployment/<name> app=image:v2  # Update image
kubectl rollout status deployment/<name>  # Watch rollout
kubectl rollout undo deployment/<name>    # Rollback

# All resources
kubectl get all                           # Get all resources
kubectl apply -f deployment.yaml          # Apply manifest
kubectl delete -f deployment.yaml         # Delete resources
```

---

## 🏗️ Architecture

### Control Plane (Master)
- **API Server**: Kubernetes API endpoint
- **etcd**: Key-value store for cluster state
- **Scheduler**: Assigns pods to nodes
- **Controller Manager**: Runs control loops

### Worker Nodes
- **kubelet**: Node agent, runs pods
- **Container Runtime**: Executes containers (Docker, containerd)
- **kube-proxy**: Network proxy, service routing

---

## Production Concerns

### Resource Management
```yaml
resources:
  requests:
    memory: "128Mi"
    cpu: "250m"
  limits:
    memory: "256Mi"
    cpu: "500m"
```

### Health Checks
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### Security
```yaml
securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  runAsNonRoot: true
  capabilities:
    drop:
    - ALL
```

### RBAC (Role-Based Access Control)
```yaml
kind: Role
metadata:
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
```

### Network Policies
```yaml
kind: NetworkPolicy
metadata:
  name: deny-all
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

### Image Security
```bash
# Scan images
trivy image myapp:1.0

# Use private registry
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com
```

---

## 📋 Practice Path

1. **Install Minikube**: Get local cluster running
2. **Deploy Nginx**: Simple pod deployment
3. **Expose Service**: Access pod from outside
4. **Add Ingress**: Route multiple services
5. **ConfigMap**: External configuration
6. **Secrets**: Sensitive data management
7. **Health Probes**: Liveness and readiness
8. **Package with Helm**: Templating and package management
9. **ArgoCD Deployment**: GitOps workflow
10. **Add Monitoring**: Prometheus + Grafana

---

## 🔗 Learning Resources

- [Minikube Handbook](https://minikube.sigs.k8s.io/docs/handbook/)
- [Kubernetes Official Tutorial](https://kubernetes.io/docs/tutorials/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [Helm Documentation](https://helm.sh/docs/)
- [12 Kubernetes Best Practices](https://kubernetes.io/blog/2016/08/kubernetes-best-practices-cluster-level-logging/)


