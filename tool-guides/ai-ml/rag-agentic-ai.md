# RAG and Agentic AI Zero to Hero Guide

## What It Is

RAG connects language models to external knowledge. Agentic AI systems use models with tools, memory, planning, and approval gates to complete workflows.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

RAG became popular as LLMs were adopted for enterprise knowledge tasks. Agentic systems expanded the pattern by giving models access to tools, structured workflows, and multi-step reasoning loops.

## Architecture and Core Concepts

RAG architecture:

```text
Documents -> Chunking -> Embeddings -> Vector DB -> Retriever -> LLM -> Answer -> Evaluation
```

Agent architecture:

```text
User goal -> Planner -> Tool call -> Observation -> Decision -> Final response
```

Key concepts:

- Prompt, embedding, vector database, retriever, tool call, memory, guardrail, evaluation.

## Zero to Hero Learning Path

1. Learn prompt engineering basics.
2. Build a simple LLM API call.
3. Create embeddings for documents.
4. Store vectors in a vector database.
5. Build retrieval and answer generation.
6. Add evaluation examples.
7. Add tool calling with approval gates.
8. Add logging, tracing, and security.

## How to Start Using It

Production AI API flow:

```text
Client -> Kong/Nginx -> AI API -> Retriever -> Vector DB -> Model Provider -> Logs/Eval
```


## Common Integrations and Pipeline Usage

Integrates with OpenAI, Anthropic, Hugging Face, LangChain, LlamaIndex, Haystack, MongoDB Atlas Vector Search, Pinecone, Weaviate, Qdrant, PostgreSQL pgvector, FastAPI, Kong, OpenTelemetry, and evaluation tools.

## Advanced Topics

- Prompt injection defense.
- RAG evaluation datasets.
- Tool permission boundaries.
- Human-in-the-loop approvals.
- Cost and latency optimization.
- LLM observability.
- Multi-agent workflow risks.

## Hands-on Project

Build a RAG chatbot over course PDFs, add citation output, evaluation questions, API gateway rate limits, and trace logs.

## Interview Questions

- What is RAG?
- What is an embedding?
- What is a vector database?
- What is tool calling?
- How do you prevent prompt injection?
- How do you evaluate an AI assistant?

## References

- [MongoDB AI Stack](https://www.mongodb.com/resources/basics/artificial-intelligence/ai-stack)
- [Kong Gateway Documentation](https://docs.konghq.com/gateway/latest/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
