# MLOps Guide

![MLOps](https://img.shields.io/badge/MLOps-Production%20ML-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)

## What It Is

MLOps brings software engineering, DevOps, data engineering, and model governance together so machine learning models can be deployed, monitored, improved, and audited in production.

## Lifecycle Architecture

```text
Data -> validation -> training -> experiment tracking -> model registry -> package -> deploy -> monitor -> retrain or rollback
```

## Learn In This Order

1. ML lifecycle and the difference between training and serving.
2. Experiment tracking: parameters, metrics, artifacts, and reproducibility.
3. Dataset and model versioning.
4. Model registry and promotion stages.
5. Batch inference vs online inference.
6. FastAPI model serving and Docker packaging.
7. CI/CD for model APIs.
8. Monitoring: latency, errors, drift, data quality, and business metrics.
9. Governance: model cards, approvals, audit logs, and rollback.

## Practical Architecture

```text
Training pipeline -> MLflow tracking -> model registry -> Docker image -> Kubernetes/cloud endpoint -> metrics/logs/drift -> retraining workflow
```

## Common Tools

- MLflow, Kubeflow, Airflow, DVC.
- Docker, Kubernetes, FastAPI.
- Amazon SageMaker AI, Azure Machine Learning, Vertex AI.
- Prometheus, Grafana, OpenTelemetry.

## Scenario Interview Questions

1. A new model is better offline but worse in production. How do you investigate data, metrics, traffic, and rollout?
2. A dependency update changed predictions. How do versioning and reproducible environments help?
3. Model endpoint latency doubled. What do you check in model, CPU/GPU, batching, autoscaling, and API logs?
4. Drift is detected. When do you retrain, rollback, or simply observe?
5. A regulator asks for prediction history. What artifacts and logs must exist?

## Official References

- https://mlflow.org/docs/latest/index.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
- https://learn.microsoft.com/en-us/azure/machine-learning/
- https://cloud.google.com/vertex-ai/docs
