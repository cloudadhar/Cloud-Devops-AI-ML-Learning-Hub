# Artificial Intelligence Engineering

![AI](https://img.shields.io/badge/AI-8B5CF6?style=for-the-badge&logo=openai&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)

## Who This Track Is For

Software engineers, cloud learners, and builders who want to create AI-powered apps without first becoming ML researchers.

## Outcomes

- Understand model providers, prompts, tokens, context windows, structured output, evaluation, latency, and cost.
- Build AI APIs with Python/FastAPI and safe request/response logging.
- Add guardrails for prompt injection, unsafe output, privacy, and human review.


## Architecture Mental Model

```text
User -> App/API -> prompt builder -> model provider/local model -> validator -> response -> logs/evals -> feedback loop
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Learn Python API basics, JSON, HTTP, and model API request/response structure.
- Write prompts with role, task, context, examples, constraints, and output format.
- Measure cost, latency, and answer quality manually.

### Days 31-60

- Build a small AI assistant API with FastAPI.
- Add structured output, retries, timeout, logging, and fallback response.
- Create an evaluation set with expected behavior and failure cases.

### Days 61-90

- Add safety filters, PII rules, prompt-injection checks, and human approval for risky actions.
- Deploy behind Nginx/Kong and monitor usage.
- Create a production upgrade plan with caching, rate limits, and tracing.

## Hands-on Labs

- Build a support ticket summarizer API.
- Build a meeting notes action extractor with JSON output.
- Create a prompt evaluation spreadsheet or JSON file with pass/fail cases.
- Deploy one AI API with logs and dashboard.

## Scenario-Based Interview Questions

1. The AI gives different answers for the same question. How do temperature, prompt, model choice, retrieval, and evaluation affect it?
2. A user tries to make the assistant reveal hidden instructions. What controls do you add?
3. The AI API is too expensive. How do caching, shorter context, model routing, and batching help?
4. A business user wants the AI to approve refunds automatically. What approval and audit controls do you require?
5. The model output breaks downstream JSON parsing. How do schema validation, retries, and fallback work?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.langchain.com/oss/python/langchain/overview
- https://fastapi.tiangolo.com/
- https://opentelemetry.io/docs/what-is-opentelemetry/
