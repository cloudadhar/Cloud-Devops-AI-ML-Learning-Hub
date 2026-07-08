# HTTP, DNS, and Load Balancing

## What Happens When You Open a Website

1. Browser checks cache.
2. DNS resolves the domain to an IP address.
3. Browser opens a TCP connection.
4. TLS handshake happens for HTTPS.
5. Browser sends HTTP request.
6. Load balancer or reverse proxy routes traffic.
7. Application returns a response.
8. Browser renders the page.

## Key Concepts

| Concept | Meaning |
| --- | --- |
| DNS | Converts names to IP addresses. |
| HTTP | Application protocol for web traffic. |
| HTTPS | HTTP over TLS encryption. |
| Reverse proxy | Receives client requests and forwards to backend services. |
| Load balancer | Distributes traffic across targets. |
| API gateway | Adds API routing, auth, rate limits, plugins, and governance. |

## Nginx and Kong Placement

```text
Client -> DNS -> Load Balancer -> Nginx/Kong -> App Service -> Database
```

Use Nginx to learn HTTP routing and reverse proxy basics. Use Kong when you need API-specific controls such as consumers, plugins, authentication, rate limiting, and observability.

## Practice Tasks

- Use `curl -I` to inspect headers.
- Use `dig` or `nslookup` to inspect DNS.
- Configure Nginx reverse proxy.
- Add Kong route and service for an API.

## References

- [MDN Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development)
- [Nginx documentation](https://nginx.org/en/docs/)
- [Kong Gateway documentation](https://docs.konghq.com/gateway/latest/)
