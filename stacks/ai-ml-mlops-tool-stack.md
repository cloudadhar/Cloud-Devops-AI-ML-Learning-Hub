# AI / ML / MLOps Tool Stack

The AI/ML stack covers data preparation, model development, training, evaluation, deployment, monitoring, and governance. For modern LLM systems, it also includes orchestration, retrieval, vector search, model providers, and safety controls.

## Core AI/ML Stack

| Layer | Purpose | Tools |
| --- | --- | --- |
| Languages | Build data and model systems | Python, SQL, JavaScript/TypeScript |
| Data storage | Store raw and processed data | S3, Google Cloud Storage, Azure Blob Storage, PostgreSQL, MongoDB, Snowflake |
| Data processing | Clean and transform data | Pandas, NumPy, Apache Spark, Dask, dbt |
| Classical ML | Train standard ML models | Scikit-learn, XGBoost, LightGBM |
| Deep learning | Train neural networks | PyTorch, TensorFlow, JAX |
| Experiment tracking | Compare runs and metrics | MLflow, Weights & Biases |
| Data and model versioning | Reproduce datasets and models | DVC, Git, model registries |
| Pipelines | Automate training and batch jobs | Airflow, Kubeflow, Prefect |
| Model serving | Expose predictions as APIs | FastAPI, BentoML, TorchServe, TensorFlow Serving, NVIDIA Triton |
| Containers and orchestration | Package and scale model services | Docker, Kubernetes |
| Cloud ML platforms | Managed training and deployment | SageMaker AI, Azure Machine Learning, Google Cloud AI documentation |
| Monitoring | Track quality, drift, latency, cost | Prometheus, Grafana, Arize, W&B, OpenTelemetry |

## Generative AI and Agentic AI Stack

| Layer | Purpose | Tools |
| --- | --- | --- |
| Model providers | LLM and embedding APIs | OpenAI, Anthropic, Google, Azure OpenAI, AWS Bedrock, Mistral AI, Cohere, Hugging Face |
| Local/open models | Local inference and experiments | Ollama, Hugging Face Transformers, vLLM |
| Orchestration | Build RAG and agent workflows | LangChain, LlamaIndex, Haystack, DSPy |
| Vector and operational databases | Store app data and embeddings | MongoDB Atlas Vector Search, Pinecone, Weaviate, Qdrant, PostgreSQL + pgvector |
| API layer | Expose AI services safely | FastAPI, Nginx, Kong AI Gateway |
| Evaluation | Test answer quality and regressions | Ragas, TruLens, prompt/version evaluation datasets |
| Observability | Trace prompts, costs, latency, failures | LangSmith, W&B, Arize, Galileo, OpenTelemetry |
| Security and governance | Control data, tools, prompts, and access | Vault, IAM, rate limits, approval gates, audit logs |

## Beginner AI App Stack

```text
Python -> FastAPI -> OpenAI/Hugging Face -> MongoDB/PostgreSQL -> Docker -> Cloud Run/App Service/EC2
```

## RAG Stack

```text
Documents -> Chunking -> Embeddings -> Vector Database -> Retriever -> LLM -> API -> Logging/Evaluation
```

## Production AI API Stack

```text
GitHub -> CI/CD -> Docker -> Kubernetes -> Kong/Nginx -> AI Service -> Vector DB -> Observability -> Evaluation -> Guardrails
```

## Learner Projects

- RAG chatbot over college PDFs.
- Resume helper with evaluation examples.
- DevOps troubleshooting assistant with command safety checks.
- Model API with MLflow tracking.
- Prompt evaluation dashboard.
- AI API behind Kong with rate limiting and logging.

## Validated References

- [MongoDB AI stack](https://www.mongodb.com/resources/basics/artificial-intelligence/ai-stack) - AI stack overview.
- [MLflow documentation](https://mlflow.org/docs/latest/index.html) - experiment tracking and model lifecycle.
- [Kubeflow documentation](https://www.kubeflow.org/docs/) - ML workflows on Kubernetes.
- [Amazon SageMaker AI documentation](https://docs.aws.amazon.com/sagemaker/) - AWS ML platform.
- [Azure Machine Learning documentation](https://learn.microsoft.com/en-us/azure/machine-learning/) - Azure ML platform.
- [Google Cloud AI documentation](https://cloud.google.com/vertex-ai/docs) - current Google Cloud AI documentation route.
- [Kong Gateway documentation](https://docs.konghq.com/gateway/latest/) - API and AI gateway documentation.
