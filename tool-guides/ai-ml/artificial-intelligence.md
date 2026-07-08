# Artificial Intelligence Engineering Guide

![AI](https://img.shields.io/badge/AI-Engineering-8B5CF6?style=for-the-badge&logo=openai&logoColor=white)

## What It Is

AI engineering is the practice of building software systems that use AI models through APIs, local models, workflows, prompts, tools, guardrails, and evaluation. It focuses on building useful applications around models, not only training models from scratch.

## Where It Fits

```text
User -> Application/API -> Prompt and context builder -> Model -> Validation -> Response -> Logs and evaluation
```

## Learn In This Order

1. Python, HTTP, JSON, environment variables, and API basics.
2. Prompt structure: role, task, context, examples, constraints, and output format.
3. Model parameters: temperature, max tokens, context length, timeout, retries, and model selection.
4. Structured outputs and validation.
5. Evaluation datasets and manual review.
6. Safety controls: prompt injection defense, PII handling, policy checks, and human approval.
7. Deployment with FastAPI, Docker, Nginx/Kong, and observability.

## Practical Architecture

```text
Client -> FastAPI -> request validation -> prompt template -> model call -> schema validation -> response -> OpenTelemetry/logs -> evaluation store
```

## Common Tools

- Python, FastAPI, Pydantic.
- LangChain or LlamaIndex for orchestration when needed.
- Local models through Ollama or remote model providers.
- Kong/Nginx for API routing, auth, and rate limits.
- OpenTelemetry, Prometheus, Grafana for visibility.

## Scenario Interview Questions

1. The AI API gives inconsistent output. How do prompt design, temperature, model choice, and evaluation affect consistency?
2. A user asks the model to reveal hidden instructions. What protections do you add?
3. The AI response must be valid JSON. How do schema validation and retry/fallback logic work?
4. Costs are increasing. How do caching, model routing, context trimming, and batching reduce cost?
5. An AI action can affect customer data. What human approval and audit controls are required?

## Official References

- https://docs.langchain.com/oss/python/langchain/overview
- https://fastapi.tiangolo.com/
- https://opentelemetry.io/docs/what-is-opentelemetry/
