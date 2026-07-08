# DevOps and Cloud Labs

## Lab 1: GitHub Actions CI

Goal: run lint/test workflow on every pull request.

Pipeline:

```text
checkout -> install -> lint -> test
```

Add later:

- Secret scanning
- Docker build
- Artifact upload

## Lab 2: Dockerized API Behind Nginx

Goal: run an API container and route traffic through Nginx.

Architecture:

```text
Browser -> Nginx -> API container
```

Interview questions:

- Why use Nginx in front of an app?
- What logs would you check first?

## Lab 3: Terraform VM Deployment

Goal: create a cloud VM using Terraform.

Required:

- Provider setup
- Variables
- Outputs
- Tags
- Cleanup with `terraform destroy`

## Lab 4: Kubernetes Deployment

Goal: deploy app to Kubernetes with service and ingress.

Add later:

- Helm chart
- Argo CD
- Prometheus metrics
- Resource limits

## Lab 5: Kong API Gateway

Goal: route an API through Kong Gateway.

Practice:

- Service
- Route
- Key authentication
- Rate limiting
- Logging plugin
