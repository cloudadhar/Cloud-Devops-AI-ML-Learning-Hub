# Kubernetes Notes

## Core Objects

| Object | Purpose |
| --- | --- |
| Pod | Smallest deployable unit. |
| Deployment | Manages replicas and rolling updates. |
| Service | Stable network access to pods. |
| Ingress | HTTP routing from outside cluster. |
| ConfigMap | Non-secret configuration. |
| Secret | Sensitive configuration. |
| Namespace | Logical grouping. |
| PersistentVolumeClaim | Storage request. |

## Basic Debug Commands

```bash
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl get svc
kubectl get ingress
kubectl get events --sort-by=.metadata.creationTimestamp
```

## Production Concerns

- Resource requests and limits
- Probes
- Security context
- RBAC
- Network policies
- Image scanning
- Ingress TLS
- Observability

## Practice Path

1. Deploy Nginx.
2. Expose using service.
3. Add ingress.
4. Add ConfigMap.
5. Add probes.
6. Package with Helm.
7. Deploy using Argo CD.
8. Add monitoring.
