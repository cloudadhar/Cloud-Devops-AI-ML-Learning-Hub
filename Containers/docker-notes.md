# Docker Notes - Complete Installation & DockerHub Guide

## 📚 Official Documentation

### Docker Official Resources
- **Docker Documentation**: https://docs.docker.com/
- **Docker Installation Guide**: https://docs.docker.com/install/
- **DockerHub Official**: https://hub.docker.com/
- **Docker CLI Reference**: https://docs.docker.com/engine/reference/commandline/
- **Dockerfile Reference**: https://docs.docker.com/engine/reference/builder/

---

## 🚀 Installing Docker

### macOS Installation

**Option 1: Docker Desktop (Recommended)**
1. Download from https://www.docker.com/products/docker-desktop
2. System Requirements:
   - macOS 11 (Big Sur) or newer
   - Apple Silicon (M1/M2) or Intel processor
   - 4GB minimum RAM (8GB recommended)
3. Double-click `Docker.dmg`
4. Drag Docker to Applications folder
5. Launch Docker from Applications
6. Verify installation:
```bash
docker --version
docker run hello-world
```

**Option 2: Homebrew**
```bash
brew install docker docker-compose
# or
brew install orbstack  # Lightweight alternative to Docker Desktop
```

### Linux Installation (Ubuntu/Debian)

```bash
# Update package manager
sudo apt-get update

# Install Docker
sudo apt-get install -y docker.io

# Add current user to docker group
sudo usermod -aG docker $USER

# Activate new group
newgrp docker

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker  # Auto-start on boot

# Verify installation
docker --version
docker run hello-world
```

**CentOS/RHEL:**
```bash
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker
```

### Windows Installation

**Option 1: Docker Desktop (Recommended)**
1. Download from https://www.docker.com/products/docker-desktop
2. System Requirements:
   - Windows 10/11 Professional or Enterprise
   - WSL 2 (Windows Subsystem for Linux 2)
   - 4GB minimum RAM
3. Run installer and follow wizard
4. Restart computer
5. Verify:
```bash
docker --version
docker run hello-world
```

**Option 2: Install WSL 2 First (if needed)**
```powershell
# Run in PowerShell as Administrator
wsl --install
# Restart computer
# Install Docker Desktop (includes WSL 2 integration)
```

---

## 📦 DockerHub Guide

### What is DockerHub?

DockerHub is Docker's official registry:
- Central repository for Docker images
- 10+ million developers
- Free and paid hosting
- Official images (Docker-verified)
- Community images
- Private repositories

**Website**: https://hub.docker.com/

### Register on DockerHub

**Step 1: Create Account**
1. Go to https://hub.docker.com/signup
2. Enter username (username stays with you, can't change)
3. Enter email address
4. Create password (strong password required)
5. Click "Sign up"
6. Verify email
7. Complete profile setup

**Step 2: Create Personal Access Token (for CLI login)**
1. Login to https://hub.docker.com
2. Click profile icon → Account Settings
3. Click "Security" → "New Access Token"
4. Give token name (e.g., "cli-login-token")
5. Copy token (you won't see it again!)
6. Save in secure location

**Step 3: Login from Terminal**
```bash
docker login -u YOUR_USERNAME
# Enter password or token when prompted
# OR use token:
docker login -u YOUR_USERNAME --password-stdin < token.txt

# Verify login
docker info
```

### Using DockerHub

**Finding Images**
```bash
# Search on DockerHub
docker search nginx
docker search python:3.9

# Or browse at https://hub.docker.com/search?q=
```

**Pulling Images from DockerHub**
```bash
# Pull official image
docker pull nginx
docker pull nginx:latest
docker pull nginx:1.21

# Pull community image
docker pull ubuntu/mysql:latest
docker pull bitnami/postgresql:latest

# Run pulled image
docker run -d -p 80:80 nginx
```

**Pushing Your Images to DockerHub**

```bash
# Step 1: Login to DockerHub
docker login

# Step 2: Tag your image
docker build -t myapp:1.0 .

# Tag with registry prefix
docker tag myapp:1.0 YOUR_USERNAME/myapp:1.0
# Example:
docker tag myapp:1.0 john/myapp:1.0

# Step 3: Push to DockerHub
docker push john/myapp:1.0

# Step 4: Create repository if needed
# Go to https://hub.docker.com → Create Repository
# Name: myapp
# Description: My application
# Public/Private: Choose visibility
# Then push as above
```

**Pulling Your Images**
```bash
docker pull john/myapp:1.0
docker run john/myapp:1.0
```

### DockerHub Repository Best Practices

```yaml
# README in your repo root explains your image
# .dockerignore to exclude files from build

# Tag versioning strategy
docker tag myapp:1.0.0 john/myapp:1.0.0      # Full version
docker tag myapp:1.0.0 john/myapp:1.0        # Minor version
docker tag myapp:1.0.0 john/myapp:latest     # Latest
docker push john/myapp:1.0.0
docker push john/myapp:1.0
docker push john/myapp:latest

# Others can now pull
docker pull john/myapp:latest
```

---

## 🏗️ Core Docker Concepts

### Image vs Container
- **Image**: packaged filesystem and metadata (blueprint)
- **Container**: running instance of an image (actual process)

### Dockerfile Components
- **FROM**: base image to build upon
- **WORKDIR**: working directory in container
- **COPY/ADD**: copy files from host to container
- **RUN**: execute commands during build
- **ENV**: environment variables
- **EXPOSE**: document which ports the container listens on
- **CMD**: default command when container starts
- **ENTRYPOINT**: container entry point

### Key Concepts
- **Volume**: persistent data storage
- **Network**: communication between containers
- **Registry**: stores images (DockerHub, ECR, Nexus, etc.)

---

## 📝 Minimal Dockerfile

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 🛠️ Useful Commands

### Image Management
```bash
docker build -t demo:local .              # Build image
docker images                              # List images
docker image ls                           # List images (newer syntax)
docker rmi image_name                     # Delete image
docker inspect image_name                 # Inspect image details
docker history image_name                 # View image layers
```

### Container Management
```bash
docker run --rm -p 8080:80 demo:local     # Run container
docker ps                                 # List running containers
docker ps -a                              # List all containers
docker logs <container>                   # View logs
docker exec -it <container> sh            # Execute command in container
docker stop <container>                   # Stop container
docker rm <container>                     # Delete container
docker stats                              # Resource usage
```

### System Commands
```bash
docker system df                          # Disk usage
docker system prune                       # Remove unused resources
docker system prune -a                    # Remove all unused resources
docker info                               # System information
```

### Registry Commands
```bash
docker login                              # Login to registry
docker logout                             # Logout from registry
docker tag image_name registry/image_name # Tag for registry
docker push registry/image_name           # Push to registry
docker pull registry/image_name           # Pull from registry
```

---

## 🐛 Common Problems & Solutions

| Problem | Cause | Solution |
| --- | --- | --- |
| App not reachable | Port not mapped | Use `-p host_port:container_port` |
| Image too large | Unnecessary layers | Use multi-stage builds |
| Secrets in image | Exposed in Dockerfile | Use build secrets, env vars |
| Container exits | App crashed | Check `docker logs` |
| Permission denied | User not in docker group | Run `sudo usermod -aG docker $USER` |
| Docker daemon not running | Service not started | `sudo systemctl start docker` |
| Can't push to DockerHub | Not logged in | Run `docker login` first |
| Image name wrong | Registry prefix missing | Tag: `registry/username/image:tag` |

---

## 🔒 Security Best Practices

1. **Use official base images**
   ```dockerfile
   FROM python:3.9-slim  # Official image
   ```

2. **Scan images for vulnerabilities**
   ```bash
   trivy image myapp:1.0
   ```

3. **Don't store secrets in Dockerfile**
   ```dockerfile
   # ❌ Wrong
   ENV DB_PASSWORD=secret123
   
   # ✅ Right
   docker run -e DB_PASSWORD=secret123 myapp:1.0
   # Or use Docker secrets for Swarm/K8s
   ```

4. **Use non-root user**
   ```dockerfile
   RUN useradd -m appuser
   USER appuser
   ```

5. **Multi-stage builds reduce size**
   ```dockerfile
   FROM python:3.9 as builder
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   FROM python:3.9-slim
   WORKDIR /app
   COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
   COPY src/ .
   CMD ["python", "app.py"]
   ```

---

## 📋 Practice Exercises

1. **Static Nginx site**
   - Create Dockerfile for static site
   - Build and run locally
   - Push to DockerHub

2. **Node.js API**
   - Containerize Node.js application
   - Use multi-stage build
   - Scan with Trivy
   - Push to DockerHub

3. **Database + App**
   - Use docker-compose
   - MySQL + Python Flask
   - Share via DockerHub

4. **CI/CD Integration**
   - Build in GitHub Actions
   - Scan with Trivy
   - Push to Nexus/DockerHub

---

## 🔗 Related Resources

- [DockerHub Official](https://hub.docker.com/)
- [Docker Docs](https://docs.docker.com/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Docker Security](https://docs.docker.com/engine/security/)


