# MLOps Engineering

![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white) ![SageMaker](https://img.shields.io/badge/SageMaker%20AI-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

## Who This Track Is For

Learners who want to put ML models into production and operate them like real software systems.

## Outcomes

- Track experiments, version datasets, register models, package model APIs, and deploy with CI/CD.
- Monitor model latency, errors, data quality, drift, and business metrics.
- Explain governance: model cards, approvals, reproducibility, rollback, and retraining.


## Architecture Mental Model

```text
Data -> validation -> training pipeline -> experiment tracking -> model registry -> image build -> deploy endpoint/batch job -> monitor -> retrain/rollback
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn ML lifecycle and difference between model training and model serving.
- Use MLflow or equivalent to log parameters, metrics, artifacts, and model versions.
- Serve a simple model with FastAPI.

### Days 31-60

- Dockerize model API and build CI pipeline with tests and image scan.
- Add model registry stages, approval, and promotion from dev to production.
- Monitor latency, error rate, and prediction distribution.

### Days 61-90

- Add drift detection, retraining trigger, shadow/canary model strategy, and rollback plan.
- Use cloud ML platforms such as SageMaker AI, Azure Machine Learning, or Vertex AI conceptually.
- Create governance documentation for compliance and responsible AI review.

## Hands-on Labs

- Train a model and track experiments in MLflow.
- Package the best model as a FastAPI Docker service.
- Create CI/CD that tests, builds, scans, and deploys the model API.
- Add monitoring dashboard and drift investigation notes.

## Scenario-Based Interview Questions

1. A new model has better offline accuracy but worse production conversion. How do you investigate?
2. Model predictions changed after a dependency update. How do environment, data, model, and artifact versioning help?
3. A model endpoint latency doubled. What do you check in app, model size, CPU/GPU, batching, network, and autoscaling?
4. A regulator asks how a production prediction was generated. What artifacts and logs must exist?
5. Data drift is detected but business metrics are stable. Do you retrain immediately or investigate first?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://mlflow.org/docs/latest/index.html
- https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
- https://learn.microsoft.com/en-us/azure/machine-learning/
- https://cloud.google.com/vertex-ai/docs
