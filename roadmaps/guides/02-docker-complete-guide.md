# Docker Complete Guide

## Table of Contents
1. [Docker Basics](#docker-basics)
2. [Installation](#installation)
3. [Docker Commands](#docker-commands)
4. [Dockerfile Creation](#dockerfile-creation)
5. [Docker Compose](#docker-compose)
6. [Docker Registry](#docker-registry)
7. [Best Practices](#best-practices)

---

## Docker Basics

### What is Docker?
Docker is a containerization platform that packages applications and dependencies into isolated containers. Containers are lightweight, portable, and consistent across environments.

### Key Concepts

**Image**: Template with application, runtime, and dependencies
**Container**: Running instance of an image
**Registry**: Repository storing images (DockerHub, ECR, ACR)
**Layer**: Each instruction in Dockerfile creates a layer
**Volume**: Persistent storage for containers
**Network**: Communication between containers

---

## Installation

### macOS
```bash
# Install Docker Desktop
brew install --cask docker

# Verify installation
docker --version
docker run hello-world
```

### Ubuntu/Debian
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker run hello-world
```

### Windows
- Download Docker Desktop from https://www.docker.com/products/docker-desktop
- Install and follow setup wizard
- Run PowerShell or Command Prompt as Administrator

---

## Docker Commands

### Basic Commands

```bash
# Check Docker version and info
docker --version
docker info

# Search images
docker search nginx

# Pull an image
docker pull ubuntu:22.04
docker pull node:18-alpine

# List local images
docker images
docker image ls

# Run a container
docker run ubuntu:22.04 echo "Hello World"

# Run container in background
docker run -d --name my-nginx nginx

# Run with port mapping
docker run -p 8080:80 nginx
# localhost:8080 maps to container port 80

# Run with environment variables
docker run -e DATABASE_URL="mysql://localhost" myapp

# Run with volume mount
docker run -v /host/path:/container/path myapp

# Run interactive container
docker run -it ubuntu:22.04 /bin/bash

# List running containers
docker ps
docker container ls

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop <container-id>
docker stop <container-name>

# Start a stopped container
docker start <container-id>

# Remove a container
docker rm <container-id>
docker rm -f <container-id>  # Force remove

# View container logs
docker logs <container-id>
docker logs -f <container-id>  # Follow logs

# Execute command in running container
docker exec -it <container-id> /bin/bash

# View container processes
docker top <container-id>

# View container resource usage
docker stats

# Inspect container details
docker inspect <container-id>
```

### Image Commands

```bash
# Build image from Dockerfile
docker build -t myapp:1.0 .
docker build -t myapp:latest -f Dockerfile.prod .

# Tag an image
docker tag myapp:1.0 myregistry/myapp:1.0

# Push to registry
docker push myregistry/myapp:1.0

# Pull from registry
docker pull myregistry/myapp:1.0

# Remove image
docker rmi <image-id>
docker rmi -f <image-id>  # Force remove

# Show image layers
docker history myapp:1.0

# Save image to file
docker save myapp:1.0 > myapp.tar

# Load image from file
docker load < myapp.tar
```

### Network Commands

```bash
# List networks
docker network ls

# Create network
docker network create mynet

# Run containers on same network
docker run -d --name app1 --network mynet myapp:1.0
docker run -d --name app2 --network mynet myapp:1.0

# Connect container to network
docker network connect mynet <container-id>

# Disconnect container from network
docker network disconnect mynet <container-id>

# Inspect network
docker network inspect mynet
```

### Volume Commands

```bash
# List volumes
docker volume ls

# Create volume
docker volume create mydata

# Run container with volume
docker run -v mydata:/data myapp

# Bind mount (local path to container path)
docker run -v /Users/username/data:/container/data myapp

# Inspect volume
docker volume inspect mydata

# Remove volume
docker volume rm mydata
```

---

## Dockerfile Creation

### Basic Dockerfile Structure

```dockerfile
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
  CMD node healthcheck.js

# Run application
CMD ["node", "server.js"]
```

### Dockerfile Instructions

```dockerfile
# FROM: Base image
FROM ubuntu:22.04

# WORKDIR: Set working directory
WORKDIR /app

# COPY: Copy from host to container
COPY source/ destination/

# ADD: Copy and extract (tar/zip)
ADD file.tar.gz /app/

# RUN: Execute command
RUN apt-get update && apt-get install -y curl

# ENV: Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# EXPOSE: Document which ports container listens
EXPOSE 3000 8080

# VOLUME: Mount points
VOLUME /data

# USER: Run commands as user
USER appuser

# HEALTHCHECK: Container health monitoring
HEALTHCHECK CMD curl localhost:3000

# CMD: Default command (can be overridden)
CMD ["node", "server.js"]

# ENTRYPOINT: Cannot be overridden
ENTRYPOINT ["python", "app.py"]

# ARG: Build-time variables
ARG BUILD_DATE
ARG VERSION=1.0
```

### Example Dockerfiles

**Node.js Application**:
```dockerfile
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY src ./src
COPY public ./public

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodejs -u 1001
USER nodejs

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD node -e "require('http').get('http://localhost:3000', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"

CMD ["node", "src/index.js"]
```

**Multi-stage Build (Optimized)**:
```dockerfile
# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY --from=builder /app/dist ./dist

USER node

EXPOSE 3000
CMD ["node", "dist/index.js"]
```

**Python Application**:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
```

**Go Application**:
```dockerfile
# Build stage
FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o app .

# Production stage
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/app .

EXPOSE 8080
CMD ["./app"]
```

---

## Docker Compose

### Installation
```bash
# macOS and Windows (included with Docker Desktop)
docker-compose --version

# Linux
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### docker-compose.yml

```yaml
version: '3.9'

services:
  # Frontend service
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: myapp-frontend
    ports:
      - "3000:3000"
    environment:
      REACT_APP_API_URL: http://backend:5000
    depends_on:
      - backend
    networks:
      - myapp-network
    restart: unless-stopped

  # Backend service
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: myapp-backend
    ports:
      - "5000:5000"
    environment:
      DATABASE_URL: postgresql://postgres:password@db:5432/myapp
      REDIS_URL: redis://cache:6379
    depends_on:
      - db
      - cache
    networks:
      - myapp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Database service
  db:
    image: postgres:15-alpine
    container_name: myapp-db
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - db_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - myapp-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Redis cache
  cache:
    image: redis:7-alpine
    container_name: myapp-cache
    ports:
      - "6379:6379"
    networks:
      - myapp-network
    restart: unless-stopped

volumes:
  db_data:

networks:
  myapp-network:
    driver: bridge
```

### Docker Compose Commands

```bash
# Start services
docker-compose up
docker-compose up -d  # Detached mode

# Build images
docker-compose build
docker-compose build --no-cache

# View running services
docker-compose ps

# View logs
docker-compose logs
docker-compose logs -f backend  # Follow backend logs

# Stop services
docker-compose stop

# Start stopped services
docker-compose start

# Restart services
docker-compose restart

# Remove stopped containers
docker-compose rm
docker-compose down  # Remove all (including volumes)

# Execute command in service
docker-compose exec backend bash

# Scale service
docker-compose up -d --scale worker=3

# Validate compose file
docker-compose config
```

---

## Docker Registry

### DockerHub

```bash
# Login to DockerHub
docker login

# Tag image for DockerHub
docker tag myapp:1.0 username/myapp:1.0
docker tag myapp:1.0 username/myapp:latest

# Push image
docker push username/myapp:1.0

# Pull image
docker pull username/myapp:1.0

# Search images
docker search myapp

# Logout
docker logout
```

### AWS ECR (Elastic Container Registry)

```bash
# Create repository
aws ecr create-repository --repository-name myapp --region us-east-1

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

# Tag image for ECR
docker tag myapp:1.0 <account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0

# Push to ECR
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0

# Pull from ECR
docker pull <account-id>.dkr.ecr.us-east-1.amazonaws.com/myapp:1.0
```

### Azure ACR (Container Registry)

```bash
# Create registry
az acr create --resource-group mygroup --name myregistry --sku Basic

# Login to ACR
az acr login --name myregistry

# Tag image for ACR
docker tag myapp:1.0 myregistry.azurecr.io/myapp:1.0

# Push to ACR
docker push myregistry.azurecr.io/myapp:1.0

# Pull from ACR
docker pull myregistry.azurecr.io/myapp:1.0
```

### Google GCR (Google Container Registry)

```bash
# Configure Docker for GCR
gcloud auth configure-docker

# Tag image for GCR
docker tag myapp:1.0 gcr.io/my-project/myapp:1.0

# Push to GCR
docker push gcr.io/my-project/myapp:1.0

# Pull from GCR
docker pull gcr.io/my-project/myapp:1.0
```

---

## Best Practices

### Image Optimization
- ✅ Use specific base image versions (not `latest`)
- ✅ Use Alpine Linux for smaller images
- ✅ Multi-stage builds for production
- ✅ Minimize layer count
- ✅ Order Dockerfile commands (least to most frequently changed)

```dockerfile
# Good: 4 layers
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
CMD ["node", "index.js"]

# Better: 5 layers but cleaner separation
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
CMD ["node", "index.js"]
```

### Security
- ✅ Run as non-root user
- ✅ Use specific base image versions
- ✅ Scan images for vulnerabilities
- ✅ Don't include secrets in images
- ✅ Use `.dockerignore` to exclude files

```dockerfile
# Run as non-root user
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && \
    addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001
COPY . .
USER nodejs
CMD ["node", "index.js"]
```

**.dockerignore**:
```
node_modules
npm-debug.log
.git
.gitignore
.env
.env.local
dist
build
.DS_Store
.vscode
.idea
```

### Resource Management
```bash
# Limit CPU and memory
docker run -m 512m --cpus 1 myapp

# Set memory swap limit
docker run -m 512m --memory-swap 1g myapp
```

### Logging
```dockerfile
# Handle logs properly
FROM node:18-alpine
# ... rest of Dockerfile ...

# Don't use CMD with shell form, use exec form
CMD ["node", "index.js"]

# Redirect logs to stdout
RUN npm config set loglevel warn
```

```bash
# View logs
docker logs <container-id>
docker logs -f <container-id>  # Follow
docker logs --tail 100 <container-id>  # Last 100 lines
```

### Development vs Production

**development**:
```dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["npm", "run", "dev"]
```

**production** (Dockerfile.prod):
```dockerfile
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER node
CMD ["node", "index.js"]
```

---

## Useful Docker Tips

### Clean Up Resources
```bash
# Remove dangling images
docker image prune

# Remove unused images
docker image prune -a

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Remove everything (images, containers, volumes, networks)
docker system prune -a
```

### Inspect and Debug
```bash
# View image layers
docker image history myapp:1.0

# Inspect image
docker image inspect myapp:1.0

# Create container from image without running
docker create myapp:1.0

# Copy files from container
docker cp <container-id>:/app/file.txt ./

# Commit container to new image
docker commit <container-id> myapp:v2
```

### Performance
```bash
# Build with BuildKit (faster, better caching)
DOCKER_BUILDKIT=1 docker build .

# Use cache mount
docker build --build-arg BUILDKIT_INLINE_CACHE=1 .

# Build specific stage (multi-stage)
docker build --target builder .
```

---

## Official Resources

- Docker Documentation: https://docs.docker.com
- Best Practices: https://docs.docker.com/develop/dev-best-practices
- Dockerfile Reference: https://docs.docker.com/engine/reference/builder
- Docker CLI Reference: https://docs.docker.com/engine/reference/commandline/cli
- Docker Hub: https://hub.docker.com

---

**Last Updated**: August 2026
**Version**: 1.0
