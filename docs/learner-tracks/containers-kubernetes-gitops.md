# Containers, Kubernetes, and GitOps

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white) ![Argo CD](https://img.shields.io/badge/Argo%20CD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white)

## Who This Track Is For

DevOps, cloud, SRE, platform, and backend learners who need to package and run applications reliably.

## Outcomes

- Build and run container images with clear Dockerfile, tags, ports, volumes, and environment variables.
- Deploy workloads to Kubernetes using Deployments, Services, Ingress, ConfigMaps, Secrets, probes, and resource limits.
- Use Helm and Argo CD for repeatable Kubernetes deployment.


## Architecture Mental Model

```text
Source code -> Dockerfile -> Image -> Registry -> Helm chart/manifests -> Argo CD -> Kubernetes API -> Pods -> Services/Ingress -> Observability
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn image vs container, Dockerfile, build context, layers, registry, compose, logs, and exec.
- Run local multi-container app with database and API.
- Write secure Dockerfile basics: small base, non-root, no secrets in image.

### Days 31-60

- Learn Kubernetes pod, deployment, service, ingress, namespace, configmap, secret, resource request/limit, and probes.
- Deploy a sample app to kind/minikube and expose it through ingress.
- Package manifests with Helm values.

### Days 61-90

- Use Argo CD to sync app from Git to Kubernetes.
- Add HPA, network policies, RBAC, PodDisruptionBudget, and monitoring.
- Create a production rollout and rollback runbook.

## Hands-on Labs

- Dockerize a Python FastAPI or Node app and push image to registry.
- Deploy app to local Kubernetes with readiness and liveness probes.
- Create Helm chart and Argo CD application.
- Break the app intentionally and debug CrashLoopBackOff, ImagePullBackOff, and 502 errors.

## Scenario-Based Interview Questions

1. A pod is in CrashLoopBackOff. What do you check in describe, logs, events, config, secrets, probes, and resource limits?
2. An image works locally but fails in Kubernetes. How do architecture, registry auth, env vars, file paths, and user permissions matter?
3. A deployment must support zero downtime. Explain rolling update, readiness probe, maxSurge, maxUnavailable, and rollback.
4. A team commits Kubernetes secrets to Git. What should happen immediately and what design should replace it?
5. Argo CD shows OutOfSync. How do you decide whether Git or cluster state is the source of truth?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.docker.com/get-started/docker-overview/
- https://kubernetes.io/docs/concepts/overview/
- https://argo-cd.readthedocs.io/en/stable/
