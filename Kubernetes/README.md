# Kubernetes Guide

## 📚 Official Documentation

- [Kubernetes Official](https://kubernetes.io/) - official Kubernetes docs
- [Kubernetes Documentation](https://kubernetes.io/docs/) - comprehensive docs
- [kubectl CLI Reference](https://kubernetes.io/docs/reference/kubectl/) - command reference
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/latest/) - API reference

---

## 🚀 Getting Started - Choose Your Path

### Option 1: Local Development (Recommended for Beginners)
👉 **[Minikube Guide](../roadmaps/guides/11-minikube-local-setup.md)** ⭐ NEW
- Single-node Kubernetes on your laptop
- Complete Docker deployment pipeline
- DevOps tools integration
- 5-minute setup

### Option 2: Cloud-Ready Setup
👉 **[Kubernetes in Production](./kubernetes-notes.md)**
- AWS EKS, Azure AKS, GCP GKE
- Multi-node clusters
- Managed services

### Option 3: Quick Testing
- Docker Desktop built-in Kubernetes
- Enable in preferences
- Quick start for existing Docker Desktop users

---

## 📋 Learning Order

1. Understand Kubernetes concepts (Pods, Deployments, Services)
2. **Set up Minikube locally** ⭐ Start here!
3. Learn ConfigMap and Secret management
4. Explore Ingress routing
5. Practice Persistent Volumes
6. Learn Namespaces and RBAC
7. Configure Health probes and resource requests
8. Package with Helm charts
9. Setup Prometheus monitoring
10. Deploy with ArgoCD (GitOps)
11. Add network policies and security
12. Troubleshoot and optimize

---

## 🛠️ Local Development Alternatives

| Tool | Best For | Setup Time | Resources |
|------|----------|-----------|-----------|
| **Minikube** | Learning, development | 5 minutes | 2GB RAM, 2 CPUs |
| Docker Desktop | Quick testing | 1 minute | Minimal |
| Kind | Multi-node testing | 5 minutes | Low-moderate |
| k3s | Edge computing | 2 minutes | Very low (512MB) |
| kubeadm | Production-like | 30 minutes | Moderate-high |

👉 **Minikube recommended for most learners!**

---

## ☁️ Cloud Kubernetes Services

| Provider | Service | Best For |
|----------|---------|----------|
| **AWS** | EKS (Elastic Kubernetes Service) | Production, high availability |
| **Azure** | AKS (Azure Kubernetes Service) | Enterprise, multi-cloud |
| **GCP** | GKE (Google Kubernetes Engine) | Developer friendly, monitoring |

---

## 📚 Comprehensive Learning Paths

### Path 1: Complete Local-to-Cloud Journey
1. **Setup Minikube locally** → [Guide](../roadmaps/guides/11-minikube-local-setup.md)
2. **Deploy applications locally**
3. **Learn IaC with Terraform** → [Guide](../roadmaps/guides/09-terraform-beginners.md)
4. **Create cloud K8s cluster**
5. **Deploy with Helm and ArgoCD**
6. **Monitor with Prometheus + Grafana** → [Guide](../roadmaps/guides/08-prometheus-grafana.md)

### Path 2: DevSecOps with Kubernetes
1. Setup Minikube
2. Integrate Docker + SonarQube
3. Add container scanning (Trivy)
4. Setup Vault for secrets
5. Deploy with security controls

### Path 3: Production-Ready Setup
1. Cloud provider account setup
2. Terraform infrastructure creation
3. Deploy managed Kubernetes
4. Setup monitoring and logging
5. Configure GitOps pipeline

---

## 📖 Practice Labs

- Deploy Nginx in Minikube
- Create multi-tier application (frontend + backend + database)
- Setup service mesh for networking
- Add readiness and liveness probes
- Package with Helm charts
- Deploy with Argo CD (GitOps)
- Add network policies and RBAC
- Configure resource limits and requests
- Setup monitoring with Prometheus
- Perform rolling updates and rollbacks

---

## 🔗 Additional Resources

### Networking & Service Mesh
- [Cilium Documentation](https://docs.cilium.io/en/stable/) - networking, security, and eBPF
- [Istio Service Mesh](https://istio.io/latest/docs/)
- [Envoy Proxy](https://www.envoyproxy.io/)

### GitOps & Deployment
- [Argo CD Documentation](https://argo-cd.readthedocs.io/en/stable/) - GitOps continuous deployment
- [Flux Documentation](https://fluxcd.io/)

### Package Management
- [Helm Documentation](https://helm.sh/docs/) - Kubernetes package manager
- [Artifact Hub](https://artifacthub.io/) - Find Helm charts

### Tools Integration
- [Prometheus Kubernetes Monitoring](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#kubernetes_sd_config)
- [Grafana Kubernetes](https://grafana.com/docs/grafana/latest/datasources/prometheus/)
- [Security Scanning with Trivy](https://aquasecurity.github.io/trivy/)

---

## Supporting Docs

- [Kubernetes Notes](kubernetes-notes.md) - Technical reference


