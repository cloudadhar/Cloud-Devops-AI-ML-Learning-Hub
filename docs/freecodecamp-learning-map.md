# freeCodeCamp Learning Map

This page collects the freeCodeCamp links shared by the community and turns them into a practical learning path for Cloud, DevOps, GitHub, AWS, Azure, AI agents, RAG, local-first AI, CI/CD, security, and foundations.

Content note: this repository does not copy freeCodeCamp article content. Each link is used as an external reference with an original learning goal, project idea, and interview outcome written for CloudAdhar learners.

Validation date: 2026-07-08

## How To Use This Page

1. Pick one goal from the quick path.
2. Read the linked freeCodeCamp article or course.
3. Open the matching [Detailed freeCodeCamp Study Guides](freecodecamp-guides/README.md).
4. Write your own notes in this repo style: concept, commands, diagram, common mistakes, interview questions.
5. Build one small lab from the project idea.
6. Add screenshots, logs, and cleanup steps to your portfolio.

## Detailed Step Guides

| Track | Detailed Guide |
| --- | --- |
| Agentic AI, RAG, local AI, MCP workflows | [Agentic AI and RAG](freecodecamp-guides/agentic-ai-and-rag.md) |
| DevOps foundations, Bash, Python, testing, prerequisites | [DevOps Foundations and Automation](freecodecamp-guides/devops-foundations-and-automation.md) |
| AWS, Azure DevOps, GitLab CI, GitHub Actions, OIDC, RBAC, homelab | [Cloud CI/CD and Security](freecodecamp-guides/cloud-cicd-and-security.md) |
| Git, GitHub, pull requests, CI troubleshooting | [Git GitHub and CI Debugging](freecodecamp-guides/git-github-ci-debugging.md) |
| Original diagrams for all submitted URLs | [Original Architecture Diagrams](freecodecamp-guides/original-architecture-diagrams.md) |

## Quick Path By Goal

| Goal | Start With | Build Next |
| --- | --- | --- |
| Learn Git and GitHub | [Git & GitHub Crash Course](https://www.freecodecamp.org/news/git-and-github-crash-course-for-beginners/) | Git workflow notes and PR practice |
| Start DevOps from zero | [DevOps Prerequisites Course](https://www.freecodecamp.org/news/devops-prerequisites-course/) | Linux, Git, networking, and CI/CD notes |
| Build practical automation | [Bash and Python DevOps Automation](https://www.freecodecamp.org/news/how-to-use-bash-python-for-real-devops-automation-handbook-with-production-use-cases/) | Backup, cleanup, deployment, and monitoring scripts |
| Build a DevOps homelab | [Local DevOps Homelab](https://www.freecodecamp.org/news/how-to-build-a-local-devops-homelab-with-docker-kubernetes-and-ansible/) | Docker, Kubernetes, Ansible, and observability setup |
| Build a production pipeline | [Production-Ready DevOps Pipeline](https://www.freecodecamp.org/news/how-to-build-a-production-ready-devops-pipeline-with-free-tools/) | CI, tests, scans, container build, and deploy gates |
| Learn AWS for DevOps | [AWS Basics for DevOps](https://www.freecodecamp.org/news/aws-basics-for-devops/) | Linux EC2 practice, IAM notes, and cleanup checklist |
| Learn Azure DevOps | [Azure Repositories at Scale](https://www.freecodecamp.org/news/how-to-organize-and-maintain-azure-repositories-at-scale/) | Repo governance and Azure pipeline standards |
| Build AI agent projects | [Local AI Agent with Tool Calling and Memory](https://www.freecodecamp.org/news/how-to-build-your-own-local-ai-agent-with-tool-calling-and-memory/) | Agent tools, memory, safety, and logs |
| Build document Q&A | [Private RAG Q&A Agent](https://www.freecodecamp.org/news/build-a-private-rag-qa-ai-agent-for-your-documents-using-langchain/) | [CloudAdhar Private RAG Project](../projects/private-rag-qa-agent/README.md) |
| Learn CI debugging | [Fix Failing GitHub PR CI](https://www.freecodecamp.org/news/how-to-fix-failing-github-pr-ci-lint-build-errors/) | CI failure runbook and troubleshooting log |

## Agentic AI, RAG, and Local AI

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| [Local AI Agent with Tool Calling and Memory](https://www.freecodecamp.org/news/how-to-build-your-own-local-ai-agent-with-tool-calling-and-memory/) | How a local agent can call tools and keep useful context between tasks. | Build a CLI agent that can read a folder, summarize files, remember preferences, and log every tool call. |
| [Private RAG Q&A Agent](https://www.freecodecamp.org/news/build-a-private-rag-qa-ai-agent-for-your-documents-using-langchain/) | Local document Q&A with retrieval, embeddings, vector storage, and citations. | Extend [Private RAG Q&A AI Agent](../projects/private-rag-qa-agent/README.md) with FastAPI, Docker, and evaluation questions. |
| [Switchback Experiments for AI Platform Features](https://www.freecodecamp.org/news/switchback-experiments-for-ai-platform-features-in-python/) | Experiment design when user-level randomization can distort platform behavior. | Create an evaluation note comparing A/B tests, switchback tests, rollout windows, guardrail metrics, and rollback rules. |
| [AI Agent That Runs LLM Experiments](https://www.freecodecamp.org/news/build-an-ai-agent-that-runs-its-own-llm-experiments-with-autoresearch/) | How agents can plan, run, and compare LLM experiments. | Build an experiment tracker for prompts, models, latency, cost, score, and final recommendation. |
| [AI-Powered Local-First Chrome Extension](https://www.freecodecamp.org/news/how-to-build-an-ai-powered-local-first-chrome-extension/) | Local-first browser AI patterns, privacy, and user-controlled data. | Design a Chrome extension architecture with local storage, background script, model gateway, and user consent checklist. |
| [Agentic Terminal Workflow with GitHub Copilot CLI and MCP Servers](https://www.freecodecamp.org/news/how-to-build-an-agentic-terminal-workflow-with-github-copilot-cli-and-mcp-servers/) | Terminal-based agent workflows, MCP server integration, and developer automation. | Create a DevOps assistant workflow for checking repo status, reading CI logs, and suggesting safe next commands. |

## DevOps Foundations and Automation

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| [Bash and Python for Real DevOps Automation](https://www.freecodecamp.org/news/how-to-use-bash-python-for-real-devops-automation-handbook-with-production-use-cases/) | When to use shell scripts, when to use Python, and how to automate production tasks. | Write scripts for log cleanup, health checks, backups, deployment verification, and report generation. |
| [Common DevOps Mistakes and How to Avoid Them](https://www.freecodecamp.org/news/how-to-avoid-devops-mistakes/) | Practical failure patterns in automation, releases, ownership, and operations. | Create a "mistake to prevention" checklist for CI/CD, observability, secrets, and rollback. |
| [Hardware, Cloud, DevOps, Networking, Security, Databases, DNS, Git, and Linux](https://www.freecodecamp.org/news/learn-hardware-cloud-devops-networking-security-databases-dns-git-and-linux/) | Broad foundation topics that every cloud and DevOps learner should know. | Use it as a foundation checklist before AWS, Azure, GCP, Docker, and Kubernetes. |
| [How DevOps Works](https://www.freecodecamp.org/news/how-devops-works/) | DevOps culture, flow, automation, feedback, and collaboration. | Write your own DevOps lifecycle diagram and explain each stage in interview language. |
| [What is DevTestOps](https://www.freecodecamp.org/news/what-is-devtestops/) | How testing practices fit into DevOps delivery. | Add test strategy, quality gates, and release confidence metrics to your pipeline notes. |
| [DevOps Engineering Course for Beginners](https://www.freecodecamp.org/news/devops-engineering-course-for-beginners/) | Beginner-friendly DevOps scope and learning direction. | Convert the course topics into weekly notes and five interview questions per topic. |
| [DevOps Prerequisites Course](https://www.freecodecamp.org/news/devops-prerequisites-course/) | Prerequisite knowledge before deeper DevOps tools. | Map prerequisites to [Foundation Knowledge Map](foundation-knowledge-map.md). |
| [Create React App DevOps Automation](https://www.freecodecamp.org/news/lets-write-create-react-app-devops-together-dc19512c6fbb/) | Older but useful example of automating repeated frontend delivery tasks. | Rebuild the concept with a modern React or Next.js app and a GitHub Actions workflow. |

## Cloud, CI/CD, Platform, and Security

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| [Azure Repositories at Scale](https://www.freecodecamp.org/news/how-to-organize-and-maintain-azure-repositories-at-scale/) | Repository organization, branch policies, naming, permissions, and large-scale governance. | Create an Azure DevOps repo governance template for teams, branches, approvals, and permissions. |
| [Azure DevOps CI/CD for Enterprise .NET](https://www.freecodecamp.org/news/cloud-native-development-with-azure-devops-ci-cd-pipelines-in-enterprise-net-applications/) | Azure DevOps pipelines, Docker image flow, AKS deployment, security, and observability. | Build a sample YAML pipeline design with build, test, scan, package, deploy, and rollback stages. |
| [Production-Ready DevOps Pipeline with Free Tools](https://www.freecodecamp.org/news/how-to-build-a-production-ready-devops-pipeline-with-free-tools/) | How to combine free tools into a usable production-style CI/CD flow. | Create a pipeline checklist: lint, test, SAST, image scan, IaC scan, deploy, smoke test, rollback. |
| [Feature Flags and RBAC in DevOps](https://www.freecodecamp.org/news/feature-flags-and-role-based-access-control-devops/#heading-why-is-rbac-important) | Why access control and controlled rollout matter in delivery workflows. | Add RBAC, feature flag rules, approval gates, and audit logs to your deployment design. |
| [AWS Basics for DevOps](https://www.freecodecamp.org/news/aws-basics-for-devops/) | Linux machine setup on AWS and basic cloud operations for DevOps learners. | Launch a temporary EC2 instance, configure SSH, install Nginx, document security group rules, and clean up. |
| [Local DevOps Homelab](https://www.freecodecamp.org/news/how-to-build-a-local-devops-homelab-with-docker-kubernetes-and-ansible/) | Build local practice infrastructure using Docker, Kubernetes, and Ansible. | Create a homelab README with topology, setup commands, troubleshooting, and teardown steps. |
| [DevOps with GitLab CI Course](https://www.freecodecamp.org/news/devops-with-gitlab-ci-course/) | GitLab CI/CD concepts and pipeline practice. | Compare GitHub Actions, GitLab CI, and Jenkins using the same sample app. |
| [Next.js on Cloudflare Workers with GitHub Actions](https://www.freecodecamp.org/news/how-to-deploy-a-full-stack-next-js-app-on-cloudflare-workers-with-github-actions-ci-cd/) | Full-stack deployment to Cloudflare Workers with GitHub Actions. | Deploy a portfolio app and document secrets, build steps, preview, production, and rollback. |
| [OIDC in GitHub Actions for AWS](https://www.freecodecamp.org/news/how-to-set-up-openid-connect-oidc-in-github-actions-for-aws/) | Secure AWS access from GitHub Actions without long-lived static keys. | Create a secure CI/CD design using IAM role trust policy, least privilege, and environment approvals. |

## Git, GitHub, and CI Troubleshooting

| Resource | Use It To Learn | CloudAdhar Practice |
| --- | --- | --- |
| [Fix Failing GitHub PR CI](https://www.freecodecamp.org/news/how-to-fix-failing-github-pr-ci-lint-build-errors/) | Systematic debugging of lint, build, and CI failures in pull requests. | Create a CI failure runbook: reproduce locally, read logs, isolate failure, patch, rerun checks, and document fix. |
| [Git & GitHub Crash Course](https://www.freecodecamp.org/news/git-and-github-crash-course-for-beginners/) | Beginner Git and GitHub workflow. | Practice clone, branch, commit, pull request, review, merge, revert, and conflict resolution. |
| [Git and GitHub Beginner-Friendly Handbook](https://www.freecodecamp.org/news/learn-how-to-use-git-and-github-a-beginner-friendly-handbook/) | Deeper beginner handbook for Git concepts and GitHub collaboration. | Create a Git command cheat sheet and explain each command with one real scenario. |

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

## Duplicate Links In The Submitted List

The submitted list contained these duplicates. They are included once in the learning map:

- [Local DevOps Homelab](https://www.freecodecamp.org/news/how-to-build-a-local-devops-homelab-with-docker-kubernetes-and-ansible/)
- [Next.js on Cloudflare Workers with GitHub Actions](https://www.freecodecamp.org/news/how-to-deploy-a-full-stack-next-js-app-on-cloudflare-workers-with-github-actions-ci-cd/)

## Validation Log

Detailed validation is recorded in [freeCodeCamp URL validation log](../logs/freecodecamp-url-validation-2026-07-08.md).
