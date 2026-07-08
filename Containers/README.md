# Containers Guide

## Topics

- Images and containers
- Dockerfile basics
- Multi-stage builds
- Volumes
- Networks
- Registries
- Image scanning
- Container runtime security
- Compose for local development
- Kubernetes for orchestration

## Commands to Practice

```bash
docker build -t app:local .
docker run --rm -p 8080:8080 app:local
docker ps
docker logs <container>
docker exec -it <container> sh
docker compose up
docker image prune
```

## Validated References

- [Docker Docs](https://docs.docker.com/) - official Docker docs.
- [Kubernetes Docs](https://kubernetes.io/docs/) - official Kubernetes docs.
