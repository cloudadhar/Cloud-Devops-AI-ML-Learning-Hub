# Platform Engineering: Nginx and Kong

![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) ![Kong](https://img.shields.io/badge/Kong-003459?style=for-the-badge&logo=kong&logoColor=white) ![Platform](https://img.shields.io/badge/Platform%20Engineering-0EA5E9?style=for-the-badge)

## Who This Track Is For

Learners who want to operate reverse proxies, ingress, API gateways, internal developer platforms, and production traffic controls.

## Outcomes

- Explain reverse proxy, load balancing, TLS termination, upstreams, ingress, routing, plugins, authentication, and rate limiting.
- Use Nginx for web/app traffic and Kong for API gateway use cases.
- Design traffic flow that includes security, observability, versioning, and rollback.


## Architecture Mental Model

```text
Client -> DNS/CDN -> Load balancer -> Nginx/Kong -> route/plugins -> upstream service -> logs/metrics/traces -> alerts
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Install Nginx, serve static content, proxy to local app, and read access/error logs.
- Learn HTTP headers, TLS, upstreams, 502/504 errors, and health checks.
- Understand API gateway vs reverse proxy.

### Days 31-60

- Run Kong locally, define services/routes, add rate limiting and key auth/JWT/OIDC conceptually.
- Use Nginx or Kong with Docker Compose microservices.
- Add structured logs and Prometheus/Grafana visibility.

### Days 61-90

- Design Kubernetes ingress and API gateway deployment model.
- Create platform standards for routing, auth, rate limits, certificates, and ownership.
- Write a production troubleshooting guide for 404, 401, 429, 502, and 504.

## Hands-on Labs

- Run a backend API behind Nginx and intentionally debug 502.
- Run Kong Gateway with one service, one route, and rate limiting.
- Add TLS locally or document production TLS flow with cert-manager/cloud certificates.
- Create an API traffic architecture diagram with observability points.

## Scenario-Based Interview Questions

1. Users get 502 Bad Gateway after deployment. How do you check upstream health, ports, DNS, logs, and timeouts?
2. An API is being abused by too many requests. How do rate limits, authentication, and logging help?
3. A team wants Nginx and Kong both. Explain which layer handles static/proxy traffic and which handles API policy.
4. TLS expires tonight. What monitoring and renewal process should exist?
5. A mobile app needs versioned APIs. How do routes, upstreams, headers, and deprecation policy help?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
- https://developer.konghq.com/gateway/
- https://kubernetes.io/docs/concepts/services-networking/ingress/
