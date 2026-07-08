# MLOps Lifecycle Notes

## Lifecycle

```text
data -> experiment -> train -> evaluate -> register -> deploy -> monitor -> retrain
```

## Data

Track:

- Source
- Schema
- Quality checks
- Version
- Privacy constraints

## Experiment

Track:

- Dataset version
- Code version
- Parameters
- Metrics
- Artifacts

Tools: MLflow, Weights & Biases.

## Deployment

Common serving choices:

- FastAPI for custom APIs.
- BentoML for packaging models.
- TensorFlow Serving or TorchServe for framework-specific serving.
- NVIDIA Triton for high-performance inference.
- SageMaker AI, Azure ML, or Google Cloud AI docs for managed platforms.

## Monitoring

Monitor:

- Latency
- Error rate
- Model quality
- Drift
- Cost
- Prompt failures for LLM apps

## Practice

- Train a small model.
- Track experiment in MLflow.
- Serve with FastAPI.
- Containerize the API.
- Add monitoring endpoint.
- Write model card and limitations.
