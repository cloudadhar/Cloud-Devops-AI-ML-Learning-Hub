# Windows Developer Setup for DevOps & Cloud Learning

Complete guide to set up your Windows machine for DevOps, Cloud, Docker, Kubernetes, and CI/CD learning.

---

## 📋 What You'll Install

By the end of this guide, you'll have:
- ✅ Git for version control
- ✅ GitHub account with SSH keys
- ✅ VS Code for coding
- ✅ Docker Desktop for containers
- ✅ WSL2 (Windows Subsystem for Linux)
- ✅ Terraform for Infrastructure as Code
- ✅ kubectl for Kubernetes management
- ✅ Package managers (Chocolatey or Scoop)
- ✅ Node.js and Python (optional but recommended)

---

## 🔧 Step 1: Install Git on Windows

### Method 1: Using Chocolatey (Recommended)

**First, install Chocolatey:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Chocolatey
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Verify installation
choco --version
```

**Then install Git:**
```powershell
choco install git -y
```

### Method 2: Using Scoop

```powershell
# Install Scoop
iwr -useb get.scoop.sh | iex

# Install Git with Scoop
scoop install git
```

### Method 3: Direct Download (Official)

1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer
3. Accept default options (recommended for beginners)
4. Verify installation in PowerShell:
   ```powershell
   git --version
   ```

### Method 4: Using Microsoft Store

```powershell
# In PowerShell
winget install git.git
```

---

## 👤 Step 2: Create GitHub Account & SSH Setup

### Create GitHub Account

1. Go to [github.com](https://github.com)
2. Click **Sign up**
3. Enter email, password, username
4. Verify email
5. Complete setup

### Generate SSH Key

**Open PowerShell and run:**

```powershell
# Generate SSH key (press Enter 3 times for defaults)
ssh-keygen -t ed25519 -C "your-email@example.com"

# For older Windows (if ed25519 not supported):
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"

# Display the public key
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

### Add SSH Key to GitHub

1. Go to [github.com/settings/keys](https://github.com/settings/keys)
2. Click **New SSH key**
3. Title: "My Windows Machine"
4. Paste the public key from PowerShell above
5. Click **Add SSH key**

### Test SSH Connection

```powershell
# Test GitHub connection
ssh -T git@github.com

# You should see:
# Hi username! You've successfully authenticated...
```

---

## 💻 Step 3: Install VS Code

### Using Chocolatey

```powershell
choco install vscode -y
```

### Using Direct Download

1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Run the installer
3. Accept defaults

### Essential VS Code Extensions

Open VS Code and install:
- **Git Graph** - Visualize Git commits
- **GitLens** - Git information inline
- **Docker** - Docker support
- **Kubernetes** - Kubernetes tools
- **Python** - Python development
- **Remote - WSL** - WSL2 integration
- **Thunder Client** - API testing
- **YAML** - YAML syntax support

```powershell
# Install extensions from command line
code --install-extension eamodio.gitlens
code --install-extension ms-vscode.remote-wsl
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-kubernetes-tools.vscode-kubernetes-tools
```

---

## 🐧 Step 4: Install WSL2 (Windows Subsystem for Linux)

WSL2 allows you to run Linux commands directly on Windows - essential for DevOps learning!

### Step 1: Enable WSL2

**Run PowerShell as Administrator:**

```powershell
# Enable WSL
wsl --install

# Or enable manually:
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# Set WSL2 as default
wsl --set-default-version 2

# Restart your computer
Restart-Computer
```

### Step 2: Install Ubuntu

**After restart, open PowerShell:**

```powershell
# Install Ubuntu 22.04
wsl --install -d Ubuntu-22.04

# Or install from Microsoft Store:
# Search "Ubuntu 22.04 LTS" in Store and click Install
```

### Step 3: Configure Ubuntu

**First launch - Set username and password:**

```bash
# You'll be prompted for a new username and password
# Create your Linux user
```

### Step 4: Update Ubuntu

```bash
# Inside WSL terminal
sudo apt update
sudo apt upgrade -y
```

### Step 5: Install Essential Tools in WSL2

```bash
# Git (already installed usually)
git --version

# Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Python
sudo apt install -y python3 python3-pip

# Terraform
wget https://releases.hashicorp.com/terraform/1.6.0/terraform_1.6.0_linux_amd64.zip
unzip terraform_1.6.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform --version

# Kubernetes CLI (kubectl)
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client

# Docker CLI (for using Docker Desktop)
sudo apt install -y docker.io
docker --version
```

### Accessing WSL2 from VS Code

1. Open VS Code
2. Click Remote icon (bottom-left)
3. Select "Connect to WSL"
4. Now you're editing directly in WSL!

---

## 🐳 Step 5: Install Docker Desktop

### Using Chocolatey

```powershell
choco install docker-desktop -y
```

### Using Direct Download

1. Download from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Run installer
3. Restart Windows
4. Open PowerShell and verify:
   ```powershell
   docker --version
   docker run hello-world
   ```

### Enable WSL2 Backend (Recommended)

In Docker Desktop Settings:
1. Go to **Settings → General**
2. Check **Use WSL 2 based engine**
3. Go to **Resources → WSL Integration**
4. Enable for your Ubuntu distro
5. Click **Apply & Restart**

---

## ☸️ Step 6: Install Kubernetes Tools

### Option 1: Minikube (Recommended for Learning)

**Using Chocolatey:**
```powershell
choco install minikube -y
choco install kubectl -y
```

**Using Direct Download:**
```powershell
# Download Minikube
$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe -OutFile minikube.exe

# Move to PATH
Move-Item .\minikube.exe C:\Windows\System32\

# Verify
minikube version
```

**Start Minikube:**
```powershell
# First start (will download Docker images)
minikube start

# Verify
kubectl get nodes
```

### Option 2: Docker Desktop Kubernetes

1. Open Docker Desktop
2. Go to **Settings → Kubernetes**
3. Check **Enable Kubernetes**
4. Wait for it to initialize
5. Verify:
   ```powershell
   kubectl get nodes
   ```

---

## 📦 Step 7: Install Terraform

### Using Chocolatey

```powershell
choco install terraform -y
terraform --version
```

### Using Direct Download

1. Download from [terraform.io/downloads](https://www.terraform.io/downloads)
2. Extract to folder
3. Add to PATH:
   ```powershell
   # Edit Environment Variables
   # Add folder path to System PATH
   ```
4. Verify:
   ```powershell
   terraform -version
   ```

---

## 🐍 Step 8: Install Python & Node.js (Optional but Recommended)

### Python via Chocolatey

```powershell
choco install python -y
python --version
pip --version

# Install useful tools
pip install --upgrade pip
pip install requests flask django
```

### Python via Direct Download

1. Download from [python.org](https://www.python.org/downloads)
2. Run installer
3. **Important**: Check **Add Python to PATH**
4. Click Install

### Node.js via Chocolatey

```powershell
choco install nodejs -y
node --version
npm --version

# Install useful tools
npm install -g yarn pnpm
```

### Node.js via Direct Download

1. Download from [nodejs.org](https://nodejs.org) (LTS version)
2. Run installer
3. Accept default options
4. Verify:
   ```powershell
   node --version
   npm --version
   ```

---

## 🛠️ Step 9: Install Additional Tools

### AWS CLI

```powershell
choco install awscli -y
aws --version

# Configure AWS credentials
aws configure
```

### Azure CLI

```powershell
choco install azure-cli -y
az --version
```

### Helm (Kubernetes package manager)

```powershell
choco install kubernetes-helm -y
helm version
```

---

## ✅ Verification Checklist

Run these commands in PowerShell to verify everything is installed:

```powershell
Write-Host "=== DevOps Tools Verification ==="
Write-Host "Git:" (git --version)
Write-Host "VS Code:" (code --version | Select-Object -First 1)
Write-Host "Docker:" (docker --version)
Write-Host "kubectl:" (kubectl version --client --short)
Write-Host "Terraform:" (terraform -version | Select-Object -First 1)
Write-Host "Python:" (python --version)
Write-Host "Node.js:" (node --version)
Write-Host "=== All Done! ==="
```

---

## 📚 First DevOps Project on Windows

### 1. Create a folder for learning
```powershell
mkdir ~/DevOps-Learning
cd ~/DevOps-Learning
git init
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

### 2. Create a simple Node.js app
```powershell
npm init -y
npm install express

# Create app.js
@"
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello from Windows DevOps Learning!');
});

app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
"@ | Out-File app.js
```

### 3. Create Dockerfile
```powershell
@"
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "app.js"]
"@ | Out-File Dockerfile
```

### 4. Build and run Docker image
```powershell
docker build -t my-devops-app .
docker run -p 3000:3000 my-devops-app

# Open browser: http://localhost:3000
```

### 5. Push to GitHub
```powershell
git add .
git commit -m "First DevOps project on Windows"
git remote add origin git@github.com:YOUR-USERNAME/devops-learning.git
git branch -M main
git push -u origin main
```

---

## 🐛 Common Windows Issues & Solutions

### Issue: "git: command not found"
**Solution**: 
- Restart PowerShell/Terminal after Git installation
- Verify Git is in PATH:
  ```powershell
  $env:Path -split ';' | Select-String "Git"
  ```

### Issue: Docker daemon not running
**Solution**:
- Make sure Docker Desktop is running
- Check system tray for Docker icon
- Restart Docker Desktop

### Issue: WSL2 not working
**Solution**:
- Enable Virtualization in BIOS
- Update Windows (Settings → Update & Security)
- Run: `wsl --update`

### Issue: SSH key permission denied
**Solution**:
```powershell
# Fix SSH key permissions
icacls $env:USERPROFILE\.ssh\id_ed25519 /inheritance:r /grant:r "$env:USERNAME`:`(F`)"
```

### Issue: Docker Desktop using too much memory
**Solution**:
1. Open Docker Desktop Settings
2. Go to **Resources → Advanced**
3. Reduce memory limit (e.g., 4GB instead of half of total)
4. Click **Apply & Restart**

---

## 🎯 Next Steps

After completing this setup guide:

1. ✅ **[01-GitHub Getting Started](./01-github-getting-started.md)** - Learn Git workflows
2. ✅ **[02-Docker Complete Guide](./02-docker-complete-guide.md)** - Master Docker
3. ✅ **[03-Nginx Web Server](./03-nginx-web-server.md)** - Web server basics
4. ✅ **[09-Terraform Beginners](./09-terraform-beginners.md)** - Infrastructure as Code
5. ✅ **[11-Minikube Local Setup](./11-minikube-local-setup.md)** - Local Kubernetes

---

## 📚 Official Windows Documentation

- [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Git for Windows](https://git-scm.com/download/win)
- [GitHub SSH Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [VS Code on Windows](https://code.visualstudio.com/docs/setup/windows)
- [Minikube on Windows](https://minikube.sigs.k8s.io/docs/start/)
- [Terraform on Windows](https://learn.hashicorp.com/tutorials/terraform/install-cli)

---

## 💡 Tips for Windows DevOps Learning

1. **Use PowerShell 7+** instead of old PowerShell (more Linux-like)
   ```powershell
   choco install powershell-core -y
   ```

2. **Use Windows Terminal** for better experience
   ```powershell
   choco install windows-terminal -y
   ```

3. **Master WSL2** - Most of DevOps work happens in Linux environment
4. **Use VS Code Remote Explorer** - Edit files in WSL directly
5. **Docker Desktop + Minikube** - Perfect for learning containers and Kubernetes
6. **Keep Docker Desktop in memory** - Essential for local development

---

**You're now ready to start DevOps learning on Windows!** 🚀

