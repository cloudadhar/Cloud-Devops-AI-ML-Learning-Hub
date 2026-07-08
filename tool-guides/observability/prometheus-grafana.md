# Prometheus and Grafana Zero to Hero Guide

## What It Is

Prometheus collects time-series metrics. Grafana visualizes metrics, logs, traces, and alerts through dashboards.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Prometheus was created at SoundCloud and open-sourced in 2012, later becoming a CNCF project. Grafana started in 2014 and became a leading dashboard platform for observability.

## Architecture and Core Concepts

Architecture:

```text
App/exporter -> Prometheus scrape -> PromQL -> Grafana dashboard -> Alertmanager notification
```

Key concepts:

- Metric name, labels, time series, scrape target.
- Exporters expose metrics.
- PromQL queries metrics.
- Grafana panels visualize queries.
- Alerts notify teams.

## Zero to Hero Learning Path

1. Run Prometheus locally.
2. Scrape a simple target.
3. Install node exporter.
4. Write PromQL queries.
5. Create Grafana dashboard.
6. Add alert rules.
7. Monitor Docker/Kubernetes apps.
8. Connect logs and traces later.

## How to Start Using It

Prometheus target pattern:

```text
Application exposes /metrics -> Prometheus scrapes -> Grafana reads Prometheus
```


## Common Integrations and Pipeline Usage

Common integration:

```text
Kubernetes -> kube-state-metrics/node-exporter/app metrics -> Prometheus -> Grafana -> Alertmanager
```

Integrates with Kubernetes, Nginx exporter, Kong metrics plugin, OpenTelemetry Collector, Loki, Tempo, Alertmanager, cloud monitoring, and incident tools.

## Advanced Topics

- PromQL rate and histogram queries.
- High-cardinality label control.
- Recording rules.
- Alert routing.
- Long-term storage.
- Grafana provisioning as code.
- SLO dashboards.

## Hands-on Project

Build a dashboard for a Dockerized API showing request count, error rate, latency, CPU, memory, and uptime.

## Interview Questions

- What are metrics?
- What is PromQL?
- Push vs pull monitoring?
- What is label cardinality?
- What should you alert on?
- How do Grafana dashboards help incidents?

## References

- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Grafana Documentation](https://grafana.com/docs/)
