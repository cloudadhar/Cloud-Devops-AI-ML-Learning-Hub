# Scenario-Based Interview Questions

Use this page for mock interviews. Scenario questions are better than definition-only questions because real jobs ask how you debug, design, secure, monitor, and communicate.

## Answer Format

```text
1. Clarify the problem and impact.
2. Draw the architecture or request path.
3. List immediate checks and evidence.
4. Explain the likely root cause.
5. Propose fix, rollback, and prevention.
6. Mention security, monitoring, and cost impact.
```

## Foundation Scenarios

1. A Linux server is reachable by ping but SSH fails. Explain how you debug network, firewall, SSH daemon, keys, user, and logs.
2. A service restarts every few seconds. Which logs and commands help you find whether it is config, permission, port, or dependency related?
3. A Git merge introduced a bug. How do you identify the commit and revert safely?
4. DNS resolves to the wrong IP for some users. Explain TTL, caching, records, and validation.
5. Disk is 100 percent full on a production server. What do you do without deleting important data blindly?

## Cloud Scenarios

1. A VM is public but the database must stay private. Design the network and security rules.
2. A cloud deployment works only from your laptop. What IAM, network, and environment assumptions do you check?
3. A bill increased 5x this month. How do you investigate and prevent recurrence?
4. A region outage affects users. Explain multi-AZ, multi-region, DNS failover, RTO, and RPO.
5. A CI/CD pipeline needs cloud access. Explain why OIDC is better than static keys.

## DevOps Scenarios

1. CI passes but deployment fails. How do you separate code build, artifact, environment, secrets, and deployment logic?
2. A production deployment must be paused after partial rollout. Explain canary, blue/green, feature flags, and rollback.
3. Jenkins queue is stuck. What do you check in agents, executors, labels, plugins, and credentials?
4. A GitHub Actions job fails only on scheduled runs. What differences from push/PR runs matter?
5. GitLab CI runners cannot pull Docker images. How do registry auth, network, image tags, and runner config affect this?

## Kubernetes Scenarios

1. A pod is `CrashLoopBackOff`. Walk through `describe`, logs, events, config, probes, resource limits, and dependencies.
2. A service returns 503 after deployment. Explain selector mismatch, endpoints, readiness, ingress, and upstream health.
3. An image is vulnerable but production needs a hotfix. What is the risk decision process?
4. Argo CD shows drift. How do you decide whether to change Git or cluster state?
5. A namespace has too many restarts. What dashboards and kubectl commands help find the pattern?

## DevSecOps Scenarios

1. A secret is committed to Git. Explain rotation, audit, history handling, prevention, and communication.
2. SAST finds a critical vulnerability right before release. How do you decide block, fix, defer, or accept risk?
3. Terraform opens port 22 to the world. Where should the control block this change?
4. A container scan reports high CVEs in base image. What do you upgrade and how do you verify?
5. A developer says security scans slow delivery. How do you design faster feedback without removing controls?

## Observability Scenarios

1. Users report slowness but CPU is normal. What metrics, logs, traces, and downstream dependencies do you inspect?
2. An alert fires frequently with no action. How do you tune the alert and define actionable signals?
3. Error rate rises after deploy. How do you correlate deployment, logs, traces, metrics, and rollback?
4. Prometheus has high cardinality. Explain labels, retention, scrape interval, and metric design.
5. A service has an SLO breach. What happens to release decisions and incident review?

## AI, ML, MLOps, and Agent Scenarios

1. An AI answer is fluent but wrong. How do you evaluate prompt, model, retrieval, and grounding?
2. A RAG system retrieves irrelevant chunks. How do chunk size, metadata, embeddings, top-k, and reranking matter?
3. A model has high offline accuracy but poor production business result. What do you investigate?
4. A model endpoint latency doubles. How do you check model size, CPU/GPU, batching, autoscaling, and dependencies?
5. An agent can call tools. What permissions, approvals, logs, and sandbox controls are required?

## Platform and Collaboration Scenarios

1. Nginx returns 502. Explain upstream, port, DNS, timeout, logs, and app health checks.
2. Kong returns 429. Explain rate limiting policy, consumer identity, route, and plugin config.
3. A Jira ticket has no acceptance criteria. What questions do you ask before implementation?
4. A release artifact was overwritten. How do versioning, immutability, promotion, and retention prevent it?
5. A Confluence runbook is outdated during incident response. How do ownership and review cadence fix the process?
