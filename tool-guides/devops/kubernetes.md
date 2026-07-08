# Kubernetes Zero to Hero Guide

## What It Is

Kubernetes orchestrates containers across a cluster, handling deployment, scaling, networking, service discovery, configuration, and self-healing.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Kubernetes was open-sourced by Google in 2014 based on lessons from internal systems. It became a CNCF project and is now the standard platform for cloud-native workloads.

## Architecture and Core Concepts

Core architecture:

```text
User -> kubectl/API Server -> Control Plane -> Scheduler/Controllers -> Nodes -> Pods
```

Key objects:

- Pod, Deployment, ReplicaSet, Service, Ingress.
- ConfigMap, Secret, Namespace, ServiceAccount.
- PersistentVolumeClaim, Job, CronJob.
- Node, control plane, container runtime, CNI, CSI.

## Zero to Hero Learning Path

1. Learn pods, deployments, and services.
2. Use kubectl to inspect resources.
3. Add ConfigMaps and Secrets.
4. Expose apps with ingress.
5. Add probes and resource limits.
6. Package apps with Helm.
7. Use Argo CD for GitOps.
8. Add monitoring, network policy, and RBAC.

## How to Start Using It

Useful commands:

```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get svc
kubectl get ingress
kubectl apply -f manifest.yaml
```


## Common Integrations and Pipeline Usage

Kubernetes production pipeline:

```text
Git -> CI -> Docker image -> Registry -> Helm chart -> Argo CD -> Kubernetes -> Prometheus/Grafana
```

Integrates with Docker, Helm, Argo CD, Flux, Nginx Ingress, Kong Ingress, cert-manager, Prometheus, Grafana, OpenTelemetry, Cilium, Istio, Vault, and cloud managed Kubernetes.

## Advanced Topics

- RBAC and service accounts.
- Network policies.
- Horizontal pod autoscaling.
- Pod disruption budgets.
- Admission controllers and policy engines.
- Cluster upgrades and backup.
- Multi-cluster GitOps.

## Hands-on Project

Deploy a microservice with Deployment, Service, Ingress, ConfigMap, Secret, probes, resource limits, Helm, and Argo CD.

## Interview Questions

- Pod vs Deployment?
- Service vs Ingress?
- ConfigMap vs Secret?
- How does Kubernetes self-healing work?
- What happens during a rolling update?
- How do you debug CrashLoopBackOff?

## References

- [Kubernetes Documentation](https://kubernetes.io/docs/)
