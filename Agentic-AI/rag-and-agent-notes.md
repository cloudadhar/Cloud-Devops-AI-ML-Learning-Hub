# RAG and Agent Notes

## RAG Flow

```text
documents -> chunk -> embed -> vector store -> retrieve -> prompt -> model -> answer -> evaluate
```

## Agent Flow

```text
user goal -> plan -> tool call -> observe -> decide -> final answer
```

## Core Components

- Model provider
- Prompt template
- Tools/functions
- Retriever
- Vector database
- Memory strategy
- Evaluation dataset
- Logs and traces
- Human approval for risky actions

## Security Rules

- Do not expose secrets to prompts.
- Validate tool inputs.
- Require approval for destructive actions.
- Log tool calls.
- Keep permissions narrow.
- Test prompt injection cases.

## Practice Projects

- PDF question-answering assistant.
- DevOps command explainer.
- Incident summary assistant.
- API documentation chatbot.
- RAG system with evaluation examples.
