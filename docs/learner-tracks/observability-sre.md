# Observability and SRE

![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white) ![OpenTelemetry](https://img.shields.io/badge/OpenTelemetry-000000?style=for-the-badge&logo=opentelemetry&logoColor=white)

## Who This Track Is For

SRE, support, DevOps, cloud operations, platform, and incident response learners.

## Outcomes

- Collect and explain metrics, logs, traces, events, alerts, SLOs, SLIs, and error budgets.
- Build dashboards that answer real operational questions instead of showing random graphs.
- Debug incidents using symptoms, impact, hypothesis, evidence, mitigation, and postmortem.


## Architecture Mental Model

```text
App -> metrics/logs/traces -> collector/exporter -> Prometheus/log store/tracing backend -> Grafana dashboards -> alerts -> incident response
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn RED and USE metrics, service health, logs, and basic Grafana dashboards.
- Install Prometheus and scrape one app or node exporter.
- Write useful alert rules with severity and runbook links.

### Days 31-60

- Add OpenTelemetry instrumentation and trace request flow through services.
- Create dashboards for latency, traffic, errors, saturation, and deployment health.
- Practice incident notes and postmortem templates.

### Days 61-90

- Define SLOs and error budget policy for a service.
- Design logging retention, trace sampling, alert routing, and on-call ownership.
- Correlate CI/CD deploy events with production metrics.

## Hands-on Labs

- Run Prometheus and Grafana locally with Docker Compose.
- Create a dashboard for app latency, error rate, CPU, memory, and restarts.
- Trigger a fake outage and write incident timeline plus action items.
- Add OpenTelemetry tracing to a small API.

## Scenario-Based Interview Questions

1. CPU is normal but users report slow checkout. What metrics and traces do you inspect first?
2. An alert fires every night but no user impact exists. How do you tune it without hiding real incidents?
3. A deployment happened 20 minutes before errors increased. How do dashboards, logs, traces, and rollback data connect?
4. Prometheus storage is growing too fast. How do labels, cardinality, retention, and scrape interval affect it?
5. A service has 99.9 percent SLO. Explain what that means for release risk and error budget.

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://prometheus.io/docs/introduction/overview/
- https://grafana.com/docs/grafana/latest/fundamentals/getting-started/first-dashboards/get-started-grafana-prometheus/
- https://opentelemetry.io/docs/what-is-opentelemetry/
