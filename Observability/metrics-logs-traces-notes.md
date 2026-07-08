# Metrics, Logs, and Traces Notes

## Metrics

Metrics are numeric measurements over time.

Examples:

- CPU usage
- Request count
- Error rate
- Latency
- Queue depth

## Logs

Logs are event records.

Examples:

- Request logs
- Error logs
- Audit logs
- Nginx access logs
- Kong gateway logs

## Traces

Traces show request flow across services.

Useful for:

- Microservices
- API gateways
- AI APIs
- Slow requests

## Golden Signals

- Latency
- Traffic
- Errors
- Saturation

## Practice

- Add request logging.
- Add Prometheus metrics.
- Build Grafana dashboard.
- Add alert for high error rate.
- Write postmortem from a simulated failure.
