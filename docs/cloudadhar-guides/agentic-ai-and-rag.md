# Agentic AI and RAG Detailed Guide

This guide covers the Agentic AI, RAG, local AI, evaluation, and MCP workflow resources from the CloudAdhar list.

## 1. Local AI Agent With Tool Calling And Memory

Reference: How to Build Your Own Local AI Agent with Tool Calling and Memory

### Learning Goal

Understand how a local AI agent can accept a user goal, decide when to call a tool, store useful context, and continue working without sending everything to a hosted model service.

### Prerequisites

- Python basics
- Virtual environments
- Basic command-line usage
- Local model runtime such as Ollama
- JSON or structured tool input/output

### Step-by-Step Learner Flow

1. Install and verify a local model runtime.
2. Create a small Python project with separate files for agent logic, tools, and memory.
3. Add one simple tool first, such as reading a file or listing a folder.
4. Define strict tool input and output formats so the agent cannot call tools randomly.
5. Add a memory store for facts that should survive across turns.
6. Add a loop: user asks, model plans, tool executes, result returns, model answers.
7. Log every tool request, tool response, final answer, and error.
8. Add safety rules for blocked commands, file boundaries, secrets, and approvals.

### Practice Lab

Build a local study assistant that can:

- Read files from a `notes/` folder
- Summarize one file
- Remember the learner's target role
- Suggest the next topic
- Write a learning log entry

### Deliverables

- Architecture diagram
- `README.md` with setup commands
- `tools.py`, `memory.py`, and `agent.py`
- Example run logs
- Safety checklist

### Interview Questions

1. What is the difference between a chatbot and a tool-calling agent?
2. Why should tool schemas be strict?
3. What should never be stored in agent memory?
4. How do you prevent an agent from executing dangerous commands?
5. How would you debug a wrong tool call?

## 2. Private RAG Q&A Agent For Documents

Reference: Build a Private RAG Q&A AI Agent for Your Documents Using LangChain

CloudAdhar project: [Private RAG Q&A AI Agent](../../projects/private-rag-qa-agent/README.md)

### Learning Goal

Build a local document Q&A system that loads private files, chunks text, creates embeddings, stores vectors, retrieves relevant context, and answers with citations.

### Prerequisites

- Python
- LangChain basics
- Ollama or another model runtime
- Embeddings
- Vector database basics
- PDF and text file handling

### Step-by-Step Learner Flow

1. Create a project folder with `documents/`, source code, requirements, and ignored generated files.
2. Add sample PDFs, Markdown files, or text notes.
3. Load documents and keep source metadata.
4. Split large documents into overlapping chunks.
5. Convert chunks into embeddings using the same model family you will use for queries.
6. Store vectors in a local vector database.
7. Convert a user question into an embedding.
8. Retrieve top matching chunks.
9. Build a prompt using only retrieved context.
10. Generate an answer and print the source files used.

### Practice Lab

Use your own Cloud, DevOps, or Kubernetes notes as documents. Ask:

- "What are the main Kubernetes components?"
- "Which file explains CI/CD stages?"
- "What should I prepare for an AWS DevOps interview?"

### Deliverables

- Working local RAG script
- Screenshot of answer with citations
- Chunking and retrieval explanation
- List of failure cases
- Production upgrade plan

### Interview Questions

1. Why is RAG not the same as fine-tuning?
2. Why do chunk size and overlap matter?
3. Why should answers include citations?
4. What happens when the answer is not present in documents?
5. How would you monitor answer quality in production?

## 3. Switchback Experiments For AI Platform Features

Reference: Switchback Experiments for AI Platform Features in Python

### Learning Goal

Learn how to test AI platform changes over time windows when simple user-level A/B testing may create unfair or noisy results.

### Prerequisites

- Python
- Basic statistics
- Experiment metrics
- Product analytics
- AI platform evaluation basics

### Step-by-Step Learner Flow

1. Identify one AI platform change, such as a new prompt, model, retriever, or ranking strategy.
2. Define the primary metric: answer quality, latency, cost, conversion, or task success.
3. Define guardrail metrics: error rate, timeout rate, unsafe answer rate, and user complaints.
4. Split time into experiment windows instead of splitting only users.
5. Alternate control and treatment windows using a predictable schedule.
6. Collect metrics for each window.
7. Compare treatment windows against nearby control windows.
8. Decide whether to ship, rollback, or run a longer test.

### Practice Lab

Create a notebook that compares two RAG chunk sizes over alternating time windows. Use a small set of repeated questions and track answer score, retrieval score, latency, and token count.

### Deliverables

- Experiment design document
- Metrics table
- Python analysis script or notebook
- Decision summary
- Rollback criteria

### Interview Questions

1. When is switchback testing better than A/B testing?
2. What is a guardrail metric?
3. Why does time-based traffic variation matter?
4. How do you avoid shipping a model that improves one metric but harms another?
5. How would you explain an inconclusive experiment?

## 4. AI Agent That Runs Its Own LLM Experiments

Reference: Build an AI Agent That Runs Its Own LLM Experiments with AutoResearch

### Learning Goal

Understand how an agent can plan experiments, execute them, compare results, and recommend the best model or prompt configuration.

### Prerequisites

- Prompt engineering
- Model comparison
- Evaluation datasets
- Python scripting
- Experiment tracking

### Step-by-Step Learner Flow

1. Define the experiment question, such as "Which prompt gives the most accurate answer?"
2. Prepare a small evaluation dataset with expected answers or grading rules.
3. Define model candidates, prompt candidates, and parameter settings.
4. Run each combination in a controlled way.
5. Store outputs, latency, token usage, cost estimate, and scores.
6. Rank results using quality and operational constraints.
7. Produce a final recommendation with evidence.
8. Save the experiment configuration so it can be repeated.

### Practice Lab

Build a prompt experiment runner for the private RAG project. Compare three system prompts and track faithfulness, citation correctness, answer length, and latency.

### Deliverables

- Experiment configuration file
- Results table
- Ranking logic
- Summary report
- Recommended prompt or model

### Interview Questions

1. Why do LLM experiments need repeatable configuration?
2. What metrics would you track besides accuracy?
3. How do you reduce bias in manual evaluation?
4. How do agents make experiment automation easier?
5. When should a human approve the final recommendation?

## 5. AI-Powered Local-First Chrome Extension

Reference: How to Build an AI-Powered Local-First Chrome Extension

### Learning Goal

Learn how to design a browser extension that keeps user data local where possible while still offering useful AI features.

### Prerequisites

- HTML, CSS, and JavaScript
- Chrome extension basics
- Local storage
- Browser permissions
- Basic AI API or local model gateway concepts

### Step-by-Step Learner Flow

1. Create the extension manifest.
2. Add popup UI for user interaction.
3. Add background or service worker logic.
4. Store user preferences locally.
5. Add a local-first data flow so private content stays on the machine unless the user approves sending it.
6. Connect to a local AI endpoint or safe AI API wrapper.
7. Add permissions only when required.
8. Add clear error handling and user consent messaging.

### Practice Lab

Build a browser extension that summarizes selected text from a web page using a local endpoint. Add a toggle for "local only" mode and a visible data usage note.

### Deliverables

- Extension folder
- Manifest file
- Popup UI
- Local storage usage
- Permission explanation
- Privacy checklist

### Interview Questions

1. What does local-first mean?
2. Why are browser extension permissions sensitive?
3. How do you protect user-selected text?
4. What should happen when the local model is unavailable?
5. How would you test a Chrome extension?

## 6. Agentic Terminal Workflow With GitHub Copilot CLI And MCP Servers

Reference: How to Build an Agentic Terminal Workflow with GitHub Copilot CLI and MCP Servers

### Learning Goal

Understand how terminal-based AI workflows can connect to external capabilities through MCP servers and help with developer or DevOps tasks.

### Prerequisites

- Terminal usage
- Git and GitHub
- Basic DevOps commands
- MCP concept
- Safe command execution habits

### Step-by-Step Learner Flow

1. Identify the repeated terminal workflow you want to improve.
2. Define what information the assistant can read.
3. Connect one MCP server or tool source at a time.
4. Ask the agent to inspect state before recommending commands.
5. Require human approval for write, deploy, delete, or secret-related operations.
6. Log prompts, tool calls, and decisions.
7. Convert repeated workflows into checklists.
8. Review permissions regularly.

### Practice Lab

Create an agentic workflow for PR troubleshooting:

- Read git status
- Inspect changed files
- Read CI failure logs
- Suggest a fix plan
- Ask for approval before editing
- Run tests
- Summarize the result

### Deliverables

- Workflow diagram
- Tool permission table
- PR troubleshooting checklist
- Sample session log
- Safety rules

### Interview Questions

1. What is MCP used for?
2. Why should agents inspect state before acting?
3. Which terminal actions need human approval?
4. How do you audit an agentic workflow?
5. How would you prevent accidental destructive commands?
