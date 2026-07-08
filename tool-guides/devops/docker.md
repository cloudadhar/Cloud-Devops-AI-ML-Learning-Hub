# Docker Zero to Hero Guide

## What It Is

Docker packages applications and dependencies into portable container images that run consistently across laptops, CI runners, servers, and Kubernetes clusters.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Docker popularized developer-friendly containers after its public launch in 2013. It made Linux container concepts easier to use through Dockerfiles, images, registries, and a simple CLI.

## Architecture and Core Concepts

Core architecture:

```text
Dockerfile -> Image -> Registry -> Container -> Logs/Networks/Volumes
```

Key concepts:

- Image, container, layer, registry, volume, network.
- Dockerfile instructions: FROM, RUN, COPY, CMD, ENTRYPOINT.
- Multi-stage builds for smaller images.
- Docker Compose for local multi-service development.

## Zero to Hero Learning Path

1. Run existing images.
2. Write a Dockerfile.
3. Build and run custom images.
4. Use environment variables and ports.
5. Use volumes for persistent data.
6. Use Docker Compose.
7. Push images to a registry.
8. Scan images and reduce image size.

## How to Start Using It

Common commands:

```bash
docker build -t app:local .
docker run --rm -p 8080:8080 app:local
docker ps
docker logs <container>
docker exec -it <container> sh
docker compose up
```


## Common Integrations and Pipeline Usage

Docker is central to CI/CD:

```text
Git -> CI -> Docker build -> Image scan -> Registry -> Kubernetes deploy
```

Integrates with GitHub Actions, GitLab CI, Jenkins, GHCR, Docker Hub, ECR, ACR, Artifact Registry, Trivy, Kubernetes, Helm, and Argo CD.

## Advanced Topics

- Multi-stage builds.
- Rootless containers.
- Image signing and SBOMs.
- BuildKit caching.
- Container networking.
- Secure base images and non-root users.

## Hands-on Project

Dockerize a FastAPI or Node.js API, add Nginx in front, build with CI, scan with Trivy, and push to a registry.

## Interview Questions

- Image vs container?
- CMD vs ENTRYPOINT?
- How does Docker layer caching work?
- Why use multi-stage builds?
- How do you debug a container that exits immediately?

## References

- [Docker Documentation](https://docs.docker.com/)
