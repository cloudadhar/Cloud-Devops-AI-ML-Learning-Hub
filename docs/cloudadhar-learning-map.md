# CloudAdhar Learning Map

This page organizes CloudAdhar learning modules into a practical path for Cloud, DevOps, GitHub, AWS, Azure, AI agents, RAG, local-first AI, CI/CD, security, and foundations.

Each module includes a learning goal, project idea, practice direction, and interview outcome for CloudAdhar learners.

Coverage date: 2026-07-08

## How To Use This Page

1. Pick one goal from the quick path.
2. Open the matching [Detailed CloudAdhar Study Guides](cloudadhar-guides/README.md).
3. Study the module outcome and practice flow.
4. Write your own notes in this repo style: concept, commands, diagram, common mistakes, interview questions.
5. Build one small lab from the project idea.
6. Add screenshots, logs, and cleanup steps to your portfolio.

## Detailed Step Guides

| Track | Detailed Guide |
| --- | --- |
| Agentic AI, RAG, local AI, MCP workflows | [Agentic AI and RAG](cloudadhar-guides/agentic-ai-and-rag.md) |
| DevOps foundations, Bash, Python, testing, prerequisites | [DevOps Foundations and Automation](cloudadhar-guides/devops-foundations-and-automation.md) |
| AWS, Azure DevOps, GitLab CI, GitHub Actions, OIDC, RBAC, homelab | [Cloud CI/CD and Security](cloudadhar-guides/cloud-cicd-and-security.md) |
| Git, GitHub, pull requests, CI troubleshooting | [Git GitHub and CI Debugging](cloudadhar-guides/git-github-ci-debugging.md) |
| Original diagrams for all CloudAdhar modules | [Original Architecture Diagrams](cloudadhar-guides/original-architecture-diagrams.md) |

## Quick Path By Goal

| Goal | Start With | Build Next |
| --- | --- | --- |
| Learn Git and GitHub | Git & GitHub Crash Course | Git workflow notes and PR practice |
| Start DevOps from zero | DevOps Prerequisites Course | Linux, Git, networking, and CI/CD notes |
| Build practical automation | Bash and Python DevOps Automation | Backup, cleanup, deployment, and monitoring scripts |
| Build a DevOps homelab | Local DevOps Homelab | Docker, Kubernetes, Ansible, and observability setup |
| Build a production pipeline | Production-Ready DevOps Pipeline | CI, tests, scans, container build, and deploy gates |
| Learn AWS for DevOps | AWS Basics for DevOps | Linux EC2 practice, IAM notes, and cleanup checklist |
| Learn Azure DevOps | Azure Repositories at Scale | Repo governance and Azure pipeline standards |
| Build AI agent projects | Local AI Agent with Tool Calling and Memory | Agent tools, memory, safety, and logs |
| Build document Q&A | Private RAG Q&A Agent | [CloudAdhar Private RAG Project](../projects/private-rag-qa-agent/README.md) |
| Learn CI debugging | Fix Failing GitHub PR CI | CI failure runbook and troubleshooting log |

## Agentic AI, RAG, and Local AI

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| Local AI Agent with Tool Calling and Memory | How a local agent can call tools and keep useful context between tasks. | Build a CLI agent that can read a folder, summarize files, remember preferences, and log every tool call. |
| Private RAG Q&A Agent | Local document Q&A with retrieval, embeddings, vector storage, and citations. | Extend [Private RAG Q&A AI Agent](../projects/private-rag-qa-agent/README.md) with FastAPI, Docker, and evaluation questions. |
| Switchback Experiments for AI Platform Features | Experiment design when user-level randomization can distort platform behavior. | Create an evaluation note comparing A/B tests, switchback tests, rollout windows, guardrail metrics, and rollback rules. |
| AI Agent That Runs LLM Experiments | How agents can plan, run, and compare LLM experiments. | Build an experiment tracker for prompts, models, latency, cost, score, and final recommendation. |
| AI-Powered Local-First Chrome Extension | Local-first browser AI patterns, privacy, and user-controlled data. | Design a Chrome extension architecture with local storage, background script, model gateway, and user consent checklist. |
| Agentic Terminal Workflow with GitHub Copilot CLI and MCP Servers | Terminal-based agent workflows, MCP server integration, and developer automation. | Create a DevOps assistant workflow for checking repo status, reading CI logs, and suggesting safe next commands. |

## DevOps Foundations and Automation

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| Bash and Python for Real DevOps Automation | When to use shell scripts, when to use Python, and how to automate production tasks. | Write scripts for log cleanup, health checks, backups, deployment verification, and report generation. |
| Common DevOps Mistakes and How to Avoid Them | Practical failure patterns in automation, releases, ownership, and operations. | Create a "mistake to prevention" checklist for CI/CD, observability, secrets, and rollback. |
| Hardware, Cloud, DevOps, Networking, Security, Databases, DNS, Git, and Linux | Broad foundation topics that every cloud and DevOps learner should know. | Use it as a foundation checklist before AWS, Azure, GCP, Docker, and Kubernetes. |
| How DevOps Works | DevOps culture, flow, automation, feedback, and collaboration. | Write your own DevOps lifecycle diagram and explain each stage in interview language. |
| What is DevTestOps | How testing practices fit into DevOps delivery. | Add test strategy, quality gates, and release confidence metrics to your pipeline notes. |
| DevOps Engineering Course for Beginners | Beginner-friendly DevOps scope and learning direction. | Convert the course topics into weekly notes and five interview questions per topic. |
| DevOps Prerequisites Course | Prerequisite knowledge before deeper DevOps tools. | Map prerequisites to [Foundation Knowledge Map](foundation-knowledge-map.md). |
| Create React App DevOps Automation | Older but useful example of automating repeated frontend delivery tasks. | Rebuild the concept with a modern React or Next.js app and a GitHub Actions workflow. |

## Cloud, CI/CD, Platform, and Security

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| Azure Repositories at Scale | Repository organization, branch policies, naming, permissions, and large-scale governance. | Create an Azure DevOps repo governance template for teams, branches, approvals, and permissions. |
| Azure DevOps CI/CD for Enterprise .NET | Azure DevOps pipelines, Docker image flow, AKS deployment, security, and observability. | Build a sample YAML pipeline design with build, test, scan, package, deploy, and rollback stages. |
| Production-Ready DevOps Pipeline with Free Tools | How to combine free tools into a usable production-style CI/CD flow. | Create a pipeline checklist: lint, test, SAST, image scan, IaC scan, deploy, smoke test, rollback. |
| Feature Flags and RBAC in DevOps | Why access control and controlled rollout matter in delivery workflows. | Add RBAC, feature flag rules, approval gates, and audit logs to your deployment design. |
| AWS Basics for DevOps | Linux machine setup on AWS and basic cloud operations for DevOps learners. | Launch a temporary EC2 instance, configure SSH, install Nginx, document security group rules, and clean up. |
| Local DevOps Homelab | Build local practice infrastructure using Docker, Kubernetes, and Ansible. | Create a homelab README with topology, setup commands, troubleshooting, and teardown steps. |
| DevOps with GitLab CI Course | GitLab CI/CD concepts and pipeline practice. | Compare GitHub Actions, GitLab CI, and Jenkins using the same sample app. |
| Next.js on Cloudflare Workers with GitHub Actions | Full-stack deployment to Cloudflare Workers with GitHub Actions. | Deploy a portfolio app and document secrets, build steps, preview, production, and rollback. |
| OIDC in GitHub Actions for AWS | Secure AWS access from GitHub Actions without long-lived static keys. | Create a secure CI/CD design using IAM role trust policy, least privilege, and environment approvals. |

## Git, GitHub, and CI Troubleshooting

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| Fix Failing GitHub PR CI | Systematic debugging of lint, build, and CI failures in pull requests. | Create a CI failure runbook: reproduce locally, read logs, isolate failure, patch, rerun checks, and document fix. |
| Git & GitHub Crash Course | Beginner Git and GitHub workflow. | Practice clone, branch, commit, pull request, review, merge, revert, and conflict resolution. |
| Git and GitHub Beginner-Friendly Handbook | Deeper beginner handbook for Git concepts and GitHub collaboration. | Create a Git command cheat sheet and explain each command with one real scenario. |

## Suggested 6-Week Learning Sprint

| Week | Focus | Deliverable |
| --- | --- | --- |
| 1 | Git, Linux, DevOps prerequisites | GitHub notes, command cheat sheet, and foundation checklist |
| 2 | Bash/Python automation | Three automation scripts with logs and README |
| 3 | CI/CD pipeline basics | GitHub Actions or GitLab CI pipeline with lint, test, build |
| 4 | Cloud deployment security | AWS OIDC or Azure DevOps pipeline design with secrets policy |
| 5 | Homelab and Kubernetes | Local Docker/Kubernetes/Ansible lab with architecture diagram |
| 6 | AI agent or RAG project | Local AI agent or document Q&A system with screenshots and interview notes |

## Interview Outcomes

After finishing these resources, learners should be able to explain:

1. Why DevOps is a delivery system, not only a tool list.
2. How CI, CD, testing, security scans, and approvals fit together.
3. Why OIDC is safer than storing cloud access keys in GitHub secrets.
4. How feature flags and RBAC reduce release risk.
5. How to debug a failing pull request pipeline step by step.
6. How a local RAG system loads documents, creates embeddings, retrieves context, and cites sources.
7. How agent memory and tool calling change the risk model of AI applications.
8. How to convert a tutorial into a portfolio-ready project with architecture, logs, cleanup, and interview notes.

## Duplicate Topics Consolidated

These repeated community topics are included once in the learning map:

- Local DevOps Homelab
- Next.js on Cloudflare Workers with GitHub Actions

## Topic Coverage Log

Detailed coverage is recorded in [CloudAdhar topic coverage log](../logs/cloudadhar-topic-validation-2026-07-08.md).
