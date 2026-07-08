# AI / ML / MLOps Labs

## Lab 1: Train and Track a Model

Goal: train a small model and track runs in MLflow.

Capture:

- Dataset version
- Parameters
- Metrics
- Model artifact

## Lab 2: Serve a Model API

Goal: expose a model using FastAPI.

Architecture:

```text
Client -> FastAPI -> Model -> Response
```

Add later:

- Docker
- Nginx
- Monitoring

## Lab 3: RAG Chatbot

Goal: answer questions from documents.

Flow:

```text
PDF -> chunks -> embeddings -> vector DB -> retriever -> LLM -> answer
```

## Lab 4: AI API Behind Kong

Goal: route an AI API through Kong Gateway with rate limiting and logs.

## Lab 5: Evaluation Dataset

Goal: create expected answers and test AI output quality over time.
