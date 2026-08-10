# Observability Guide

## Pillars of Observability

- **Metrics**: Numeric measurements over time
- **Logs**: Event records and debugging information
- **Traces**: Request flow across distributed systems
- **Events**: System state changes
- **Alerts**: Notifications for critical conditions
- **Dashboards**: Visualizations and monitoring
- **SLOs and error budgets**: Service level objectives and reliability targets

## Tools

### Metrics & Monitoring
- Prometheus
- Grafana
- Datadog
- New Relic
- CloudWatch (AWS)
- Azure Monitor
- Google Cloud Monitoring

### Logs & Aggregation
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Grafana Loki
- OpenSearch
- Splunk
- Sumo Logic
- CloudWatch Logs
- Google Cloud Logging

### Tracing & APM
- Jaeger
- Grafana Tempo
- Zipkin
- Datadog APM
- New Relic APM
- AWS X-Ray
- OpenTelemetry

### API Gateway & Reverse Proxy Monitoring
- Kong Gateway analytics and plugins
- Nginx access and error logs
- Envoy proxy metrics

## Learning Order

1. Understand metrics, labels, and time series.
2. Scrape app metrics with Prometheus.
3. Build Grafana dashboards.
4. Add log aggregation with Loki or ELK.
5. Add distributed tracing with Jaeger or Tempo.
6. Define SLI, SLO, and alert rules.
7. Write an incident postmortem.
8. Add API gateway metrics and reverse proxy logs to the dashboard.

## Official Documentation

### Metrics & Monitoring
- **Prometheus Overview**: https://prometheus.io/docs/introduction/overview/
- **Prometheus Docs**: https://prometheus.io/docs/
- **Prometheus Installation**: https://prometheus.io/download/
- **PromQL Query Language**: https://prometheus.io/docs/prometheus/latest/querying/basics/
- **Grafana Docs**: https://grafana.com/docs/
- **Grafana Dashboards**: https://grafana.com/grafana/dashboards/
- **Grafana Cloud**: https://grafana.com/products/cloud/

### Logs & Log Aggregation
- **ELK Stack Guide**: https://www.elastic.co/guide/index.html
- **Elasticsearch Docs**: https://www.elastic.co/guide/en/elasticsearch/reference/current/
- **Kibana Documentation**: https://www.elastic.co/guide/en/kibana/current/
- **Grafana Loki**: https://grafana.com/docs/loki/latest/
- **Loki Configuration**: https://grafana.com/docs/loki/latest/configuration/
- **OpenSearch**: https://opensearch.org/docs/latest/

### Tracing & Distributed Systems
- **Jaeger Documentation**: https://www.jaegertracing.io/docs/
- **Grafana Tempo**: https://grafana.com/docs/tempo/latest/
- **Zipkin Documentation**: https://zipkin.io/pages/quickstart.html
- **OpenTelemetry Docs**: https://opentelemetry.io/docs/
- **OpenTelemetry Instrumentation**: https://opentelemetry.io/docs/instrumentation/

### Alert Management
- **Prometheus AlertManager**: https://prometheus.io/docs/alerting/latest/alertmanager/
- **AlertManager Configuration**: https://prometheus.io/docs/alerting/latest/configuration/
- **Grafana Alerting**: https://grafana.com/docs/grafana/latest/alerting/

### Cloud-Native Observability
- **AWS CloudWatch**: https://docs.aws.amazon.com/cloudwatch/
- **Azure Monitor**: https://learn.microsoft.com/en-us/azure/azure-monitor/
- **Google Cloud Monitoring**: https://cloud.google.com/monitoring/docs
- **Kubernetes Monitoring**: https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/

### Standards & Best Practices
- **OpenTelemetry**: https://opentelemetry.io/
- **OpenMetrics**: https://openmetrics.io/
- **SLO & Error Budgets**: https://sre.google/sre-book/service-level-objectives/

## Validated References

- [Prometheus Overview](https://prometheus.io/docs/introduction/overview/) - official Prometheus docs.
- [Grafana Docs](https://grafana.com/docs/) - official Grafana docs.
- [OpenTelemetry Docs](https://opentelemetry.io/docs/) - official OpenTelemetry docs.
- [ELK Stack](https://www.elastic.co/guide/index.html) - official Elasticsearch documentation.
- [Jaeger](https://www.jaegertracing.io/docs/) - official Jaeger documentation.
- [Loki](https://grafana.com/docs/loki/latest/) - official Loki documentation.

## Supporting Docs

- [Metrics, Logs, and Traces Notes](metrics-logs-traces-notes.md)


