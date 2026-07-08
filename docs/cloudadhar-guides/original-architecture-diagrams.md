# Original Architecture Diagrams For Submitted CloudAdhar Topics

These diagrams are CloudAdhar learning visuals created for this repository. Use them with the detailed study guides to understand the architecture, workflow, and implementation sequence for each module.

Source map: [CloudAdhar Learning Map](../cloudadhar-learning-map.md)

Detailed guides:

- [Agentic AI and RAG](agentic-ai-and-rag.md)
- [DevOps Foundations and Automation](devops-foundations-and-automation.md)
- [Cloud CI/CD and Security](cloud-cicd-and-security.md)
- [Git GitHub and CI Debugging](git-github-ci-debugging.md)

## Agentic AI, RAG, And Local AI

### 1. Local AI Agent With Tool Calling And Memory

```mermaid
flowchart LR
    U[User goal] --> A[Local agent loop]
    A --> P[Planner]
    P --> T{Need tool?}
    T -->|Yes| S[Tool schema check]
    S --> G[Guardrails and approval]
    G --> X[Run safe tool]
    X --> O[Tool output]
    O --> A
    T -->|No| R[Generate response]
    A --> M[(Memory store)]
    M --> A
    R --> L[Answer plus action log]
```

Learner build flow:

1. Start with one safe tool.
2. Add memory only for useful non-secret facts.
3. Log tool call, input, output, and final answer.
4. Add approval before write, delete, deploy, or command execution.

### 2. Private RAG Q&A Agent For Documents

```mermaid
flowchart TD
    D[PDF, Markdown, text files] --> L[Document loader]
    L --> C[Chunk with overlap]
    C --> E[Embedding model]
    E --> V[(Vector database)]
    Q[User question] --> QE[Question embedding]
    QE --> R[Similarity search]
    V --> R
    R --> K[Top-k chunks]
    K --> P[Prompt with context]
    P --> M[Local LLM]
    M --> A[Answer with citations]
```

Learner build flow:

1. Load private documents.
2. Split into chunks.
3. Embed chunks and store vectors.
4. Retrieve top matches for each question.
5. Generate grounded answers with source names.

### 3. Switchback Experiments For AI Platform Features

```mermaid
flowchart LR
    W1[Window 1 Control] --> M1[Collect metrics]
    W2[Window 2 Treatment] --> M2[Collect metrics]
    W3[Window 3 Control] --> M3[Collect metrics]
    W4[Window 4 Treatment] --> M4[Collect metrics]
    M1 --> C[Compare nearby windows]
    M2 --> C
    M3 --> C
    M4 --> C
    C --> D{Decision}
    D -->|Better and safe| Ship[Ship feature]
    D -->|Risky| Rollback[Rollback]
    D -->|Unclear| Extend[Run longer test]
```

Learner build flow:

1. Define treatment and control behavior.
2. Alternate behavior by time window.
3. Track primary and guardrail metrics.
4. Compare nearby windows before deciding.

### 4. AI Agent That Runs LLM Experiments

```mermaid
flowchart TD
    G[Experiment goal] --> C[Candidate prompts and models]
    C --> R[Runner agent]
    R --> T[Test dataset]
    R --> O[Model outputs]
    O --> S[Scoring]
    S --> DB[(Experiment results)]
    DB --> Rank[Rank by quality, latency, cost]
    Rank --> Rec[Recommendation report]
    Rec --> H[Human approval]
```

Learner build flow:

1. Create test questions.
2. Run prompt and model combinations.
3. Score quality, citations, latency, and cost.
4. Pick a winner with evidence.

### 5. AI-Powered Local-First Chrome Extension

```mermaid
flowchart LR
    Page[Browser page] --> Select[Selected text]
    Select --> Popup[Extension popup]
    Popup --> Consent{User approval}
    Consent -->|Local only| Local[Local model gateway]
    Consent -->|Allowed API| API[Remote AI API wrapper]
    Local --> Result[Summary or action]
    API --> Result
    Popup --> Store[(Local storage)]
    Result --> UI[Show result in extension UI]
```

Learner build flow:

1. Define extension permissions.
2. Store settings locally.
3. Ask before sending page content anywhere.
4. Handle local model unavailable errors.

### 6. Agentic Terminal Workflow With GitHub Copilot CLI And MCP Servers

```mermaid
flowchart TD
    Dev[Developer request] --> Agent[Terminal assistant]
    Agent --> State[Inspect repo state]
    State --> MCP[MCP tools and servers]
    MCP --> Logs[CI logs, files, issues, docs]
    Logs --> Plan[Proposed safe plan]
    Plan --> Approval{Human approval}
    Approval -->|Approved| Action[Run command or edit]
    Approval -->|Rejected| Revise[Revise plan]
    Action --> Verify[Run checks]
    Verify --> Summary[Summarize result]
```

Learner build flow:

1. Inspect before acting.
2. Use tools with limited permissions.
3. Ask approval for risky actions.
4. Verify and summarize.

## DevOps Foundations And Automation

### 7. Bash And Python For Real DevOps Automation

```mermaid
flowchart LR
    Task[Ops task] --> Manual[Run manually once]
    Manual --> Bash[Bash script for shell flow]
    Bash --> Need{Need APIs, JSON, reports, retries?}
    Need -->|Yes| Python[Python automation]
    Need -->|No| Harden[Harden Bash]
    Python --> Safe[Dry run, logs, exit codes]
    Harden --> Safe
    Safe --> Schedule[Cron, CI, or runbook]
```

### 8. Common DevOps Mistakes And Prevention

```mermaid
flowchart TD
    Mistake[Common mistake] --> Impact[Production impact]
    Impact --> Prevention[Preventive control]
    Prevention --> Detection[Monitoring or test signal]
    Detection --> Recovery[Rollback or runbook]
    Recovery --> Learn[Post-incident learning]
    Learn --> Prevention
```

### 9. Foundation Map For Hardware, Cloud, DevOps, Networking, Security, Databases, DNS, Git, And Linux

```mermaid
flowchart TB
    Hardware[Hardware resources] --> Linux[Linux OS]
    Linux --> Network[Networking and DNS]
    Network --> Web[HTTP and load balancing]
    Linux --> Git[Git and collaboration]
    Web --> Cloud[Cloud service models]
    Cloud --> Security[IAM, secrets, encryption]
    Cloud --> Data[Databases and backups]
    Security --> DevOps[DevOps delivery]
    Data --> DevOps
```

### 10. How DevOps Works

```mermaid
flowchart LR
    Plan --> Code --> Build --> Test --> Release --> Deploy --> Operate --> Monitor --> Feedback
    Feedback --> Plan
```

### 11. DevTestOps Flow

```mermaid
flowchart LR
    Commit[Code commit] --> Unit[Unit tests]
    Unit --> Integration[Integration tests]
    Integration --> Security[Security tests]
    Security --> Build[Build artifact]
    Build --> Deploy[Deploy test env]
    Deploy --> Smoke[Smoke tests]
    Smoke --> Promote{Promote?}
    Promote -->|Yes| Prod[Production]
    Promote -->|No| Fix[Fix and retry]
```

### 12. Beginner DevOps Engineering Path

```mermaid
flowchart TD
    Linux[Linux basics] --> Git[Git and GitHub]
    Git --> Script[Bash or Python scripting]
    Script --> CI[CI/CD basics]
    CI --> Docker[Docker]
    Docker --> Cloud[Cloud deployment]
    Cloud --> Observe[Monitoring and logs]
    Observe --> Project[End-to-end portfolio project]
```

### 13. DevOps Prerequisites Path

```mermaid
flowchart LR
    Terminal --> Files[Files and permissions]
    Files --> Users[Users and groups]
    Users --> Packages[Packages and services]
    Packages --> Network[Ports, DNS, SSH]
    Network --> Git[Git workflow]
    Git --> Env[Environment variables]
    Env --> Cloud[Cloud fundamentals]
```

### 14. Frontend DevOps Automation

```mermaid
flowchart LR
    Dev[Frontend code] --> Lint[Lint and format]
    Lint --> Test[Component or unit tests]
    Test --> Build[Production build]
    Build --> Artifact[Static assets]
    Artifact --> Deploy[Deploy to hosting]
    Deploy --> Verify[Smoke test topic]
```

## Cloud, CI/CD, Security, And Platforms

### 15. Azure Repositories At Scale

```mermaid
flowchart TD
    Org[Azure DevOps organization] --> Projects[Projects]
    Projects --> Repos[Repositories]
    Repos --> Naming[Naming standards]
    Repos --> Branch[Branch policies]
    Repos --> Permissions[Team permissions]
    Repos --> Templates[README, PR, issue templates]
    Branch --> Review[Required reviewers]
    Branch --> Build[Build validation]
```

### 16. Azure DevOps Enterprise CI/CD

```mermaid
flowchart LR
    Commit --> Restore[Restore dependencies]
    Restore --> Build[Build app]
    Build --> Tests[Run tests]
    Tests --> Scan[Code and image scans]
    Scan --> Image[Build container image]
    Image --> Registry[Push to registry]
    Registry --> Deploy[Deploy to AKS or app service]
    Deploy --> Smoke[Smoke tests]
    Smoke --> Monitor[Monitor release]
```

### 17. Production-Ready DevOps Pipeline With Free Tools

```mermaid
flowchart LR
    PR[Pull request] --> Lint
    Lint --> Tests
    Tests --> SecretScan[Secret scan]
    SecretScan --> DepScan[Dependency scan]
    DepScan --> DockerBuild[Docker build]
    DockerBuild --> ImageScan[Image scan]
    ImageScan --> DeployTest[Deploy test]
    DeployTest --> Smoke[Smoke test]
    Smoke --> Promote[Promote with approval]
```

### 18. Feature Flags And RBAC In DevOps

```mermaid
flowchart TD
    User --> Auth[Authenticate]
    Auth --> Role[Resolve role]
    Role --> RBAC{Allowed action?}
    RBAC -->|No| Deny[Deny and audit]
    RBAC -->|Yes| Flag{Feature enabled?}
    Flag -->|No| Hidden[Hide feature]
    Flag -->|Yes| Feature[Use feature]
    Feature --> Audit[Audit event]
```

### 19. AWS Basics For DevOps

```mermaid
flowchart TD
    Account[AWS account with MFA] --> IAM[IAM role or user]
    IAM --> EC2[Launch EC2]
    EC2 --> SG[Security group rules]
    SG --> SSH[SSH access]
    SSH --> Install[Install Nginx or Docker]
    Install --> Verify[Verify service]
    Verify --> Logs[Check logs]
    Logs --> Cleanup[Stop or terminate resources]
```

### 20. Local DevOps Homelab With Docker, Kubernetes, And Ansible

```mermaid
flowchart TD
    Laptop[Local laptop] --> Docker[Docker runtime]
    Docker --> Cluster[kind, minikube, or k3d]
    Cluster --> App[Sample app deployment]
    App --> Ansible[Ansible setup automation]
    Cluster --> Monitor[Metrics and logs]
    App --> Ingress[Ingress or local port]
    Monitor --> Runbook[Troubleshooting runbook]
    Runbook --> Cleanup[Teardown commands]
```

### 21. DevOps With GitLab CI

```mermaid
flowchart LR
    Push[Git push] --> GitLab[GitLab CI]
    GitLab --> Runner[Runner picks job]
    Runner --> Build
    Build --> Test
    Test --> Package
    Package --> Artifacts[Artifacts and reports]
    Artifacts --> Deploy[Deploy job]
    Deploy --> Manual[Manual approval if needed]
```

### 22. Next.js On Cloudflare Workers With GitHub Actions

```mermaid
flowchart LR
    Code[Next.js code] --> GitHub[GitHub repo]
    GitHub --> Actions[GitHub Actions]
    Actions --> Install[Install dependencies]
    Install --> Build[Build for Cloudflare runtime]
    Build --> Secrets[Use deployment secrets]
    Secrets --> Cloudflare[Deploy to Cloudflare Workers]
    Cloudflare --> topic[Preview or production topic]
    topic --> Verify[Verify routes and logs]
```

### 23. OIDC In GitHub Actions For AWS

```mermaid
sequenceDiagram
    participant GH as GitHub Actions
    participant OIDC as GitHub OIDC Provider
    participant AWS as AWS STS
    participant IAM as IAM Role
    participant SVC as AWS Service
    GH->>OIDC: Request OIDC token
    OIDC-->>GH: Signed identity token
    GH->>AWS: Assume role with token
    AWS->>IAM: Validate trust policy
    IAM-->>AWS: Allow scoped session
    AWS-->>GH: Temporary credentials
    GH->>SVC: Run allowed deployment action
```

## Git, GitHub, And CI Debugging

### 24. Fix Failing GitHub PR CI

```mermaid
flowchart TD
    PR[Pull request] --> Fail[Failing check]
    Fail --> Logs[Open job logs]
    Logs --> FirstError[Find first real error]
    FirstError --> Reproduce[Run same command locally]
    Reproduce --> Fix[Make smallest fix]
    Fix --> LocalCheck[Run local check]
    LocalCheck --> Push[Push commit]
    Push --> CI[CI reruns]
    CI --> Summary[Write root cause summary]
```

### 25. Git And GitHub Crash Course

```mermaid
flowchart LR
    Init[git init or clone] --> Status[git status]
    Status --> Add[git add]
    Add --> Commit[git commit]
    Commit --> Branch[git branch]
    Branch --> Push[git push]
    Push --> PR[Open pull request]
    PR --> Review[Review and merge]
    Review --> Pull[git pull latest]
```

### 26. Git And GitHub Beginner Handbook

```mermaid
flowchart TD
    Main[Main branch] --> FeatureA[Developer A branch]
    Main --> FeatureB[Developer B branch]
    FeatureA --> PRA[Pull request A]
    FeatureB --> PRB[Pull request B]
    PRA --> ReviewA[Code review]
    PRB --> ReviewB[Code review]
    ReviewA --> MergeA[Merge]
    ReviewB --> Conflict{Conflict?}
    Conflict -->|Yes| Resolve[Resolve conflict]
    Conflict -->|No| MergeB[Merge]
    Resolve --> MergeB
```

## Portfolio Rule

For each diagram, learners should add their own:

1. Screenshot of implementation.
2. Commands used.
3. Logs or pipeline output.
4. Errors faced and fixes.
5. Interview explanation in 5 to 8 bullet points.
