# Docker Notes

## Core Concepts

- Image: packaged filesystem and metadata.
- Container: running instance of an image.
- Dockerfile: build instructions.
- Volume: persistent data mount.
- Network: communication layer for containers.
- Registry: stores images.

## Minimal Dockerfile

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
```

## Useful Commands

```bash
docker build -t demo:local .
docker run --rm -p 8080:80 demo:local
docker ps
docker logs <container>
docker exec -it <container> sh
docker image ls
docker system df
```

## Common Problems

| Problem | Check |
| --- | --- |
| App not reachable | Port mapping, app bind address, firewall |
| Image too large | Multi-stage build, base image |
| Secrets in image | Dockerfile, build args, history |
| Container exits | Logs, command, missing env vars |

## Practice

- Containerize a static Nginx site.
- Containerize a Node.js API.
- Push image to a registry.
- Scan image with Trivy.
