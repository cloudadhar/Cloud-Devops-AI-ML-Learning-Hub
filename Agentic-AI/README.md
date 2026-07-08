# Agentic AI Guide

## Concepts

- LLM basics
- Prompt engineering
- Tool calling
- Function calling
- Retrieval augmented generation
- Agents and workflows
- Memory
- Planning and reflection
- Human approval gates
- Evaluation and safety
- Observability for agent runs
- Security for tool-using systems

## Build Order

1. Prompt-only assistant
2. Assistant with structured outputs
3. RAG assistant over documents
4. Tool-calling assistant
5. Multi-step workflow assistant
6. Human-in-the-loop approval
7. Evaluation dataset
8. Logs and traces
9. Security and permission boundaries

## Projects

- College FAQ agent
- Cloud cost explainer agent
- DevOps troubleshooting assistant
- Pull request summary agent
- Incident report drafting agent
- Resume feedback agent

## Safety Checklist

- Never expose secrets to the model.
- Log tool calls and outputs.
- Require approval for destructive actions.
- Validate generated commands before execution.
- Add tests and evaluation examples.
- Keep system prompts and policies versioned.
