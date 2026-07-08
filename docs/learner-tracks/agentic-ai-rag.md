# Agentic AI and RAG

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-000000?style=for-the-badge) ![Chroma](https://img.shields.io/badge/Chroma-Vector%20DB-7C3AED?style=for-the-badge)

## Who This Track Is For

AI builders, DevOps learners exploring AI automation, and students building document Q&A or tool-calling agents.

## Outcomes

- Build RAG systems with loaders, chunking, embeddings, vector databases, retrieval, model generation, and citations.
- Build tool-calling agents with memory, approval gates, logs, and clear permission boundaries.
- Explain prompt injection, retrieval quality, evaluation, and production risks.


## Architecture Mental Model

```text
Documents -> loader -> splitter -> embeddings -> vector database -> retriever -> prompt -> LLM -> answer with citations -> evaluation logs
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Build a local document Q&A prototype with markdown/text/PDF notes.
- Understand embeddings, similarity search, chunk size, top-k retrieval, and citations.
- Create a small evaluation set of expected answers.

### Days 31-60

- Add FastAPI endpoint, Dockerfile, persistent vector DB, and source citation output.
- Add tool-calling workflow with read-only tools first.
- Log prompts, retrieved chunks, latency, model, and answer quality.

### Days 61-90

- Add prompt injection tests, allowlisted tools, human approval, rate limits, and observability.
- Evaluate retrieval quality using answer correctness, groundedness, and citation usefulness.
- Design production upgrade path with gateway, auth, secrets, monitoring, and rollback.

## Hands-on Labs

- Complete the Private RAG Q&A AI Agent project in this repo.
- Add new document type support and rebuild vector index.
- Add API endpoint and Docker Compose.
- Create an interview diagram and explain every component.

## Scenario-Based Interview Questions

1. RAG returns confident but wrong answers. How do you debug chunks, embeddings, top-k, prompt, model, and citations?
2. A document contains malicious instructions telling the agent to ignore rules. What is your defense design?
3. The vector database grows and retrieval slows. What indexing, filtering, metadata, and storage choices matter?
4. An agent can run shell commands. What approvals, allowlists, audit logs, and sandboxing are required?
5. Users want citations. How do you store source metadata and verify the answer is grounded?

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.langchain.com/oss/python/langchain/overview
- https://docs.trychroma.com/
- https://opentelemetry.io/docs/what-is-opentelemetry/
