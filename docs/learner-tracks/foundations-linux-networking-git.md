# Foundations: Linux, Networking, Git

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

## Who This Track Is For

Absolute beginners, support engineers, cloud beginners, DevOps beginners, security learners, and AI/ML learners who need command-line confidence.

## Outcomes

- Use Linux commands for files, processes, services, logs, permissions, packages, SSH, and troubleshooting.
- Explain DNS, HTTP, HTTPS, TCP, UDP, ports, load balancing, proxying, and TLS at interview level.
- Use Git and GitHub for branching, pull requests, merge conflicts, revert, tags, and collaboration.


## Architecture Mental Model

```text
User -> DNS -> Network -> Linux host -> Process/service -> Logs -> Git repo -> Pull request -> Review -> Merge
```

## 30-60-90 Day Learning Flow

### First 30 Days

- Practice daily Linux navigation, file editing, permissions, service status, process checks, and log reading.
- Draw what happens when a browser opens a URL.
- Learn Git clone, branch, commit, push, pull, merge, rebase basics, and conflict resolution.

### Days 31-60

- Create shell scripts for backup, cleanup, health check, and log summary.
- Build a static website and serve it locally.
- Create a GitHub portfolio repo with notes, screenshots, and troubleshooting logs.

### Days 61-90

- Debug a failed service using system logs, port checks, process checks, and config validation.
- Explain DNS, reverse proxy, firewall, TLS, and load balancer flow together.
- Review pull requests and write proper commit messages and rollback notes.

## Hands-on Labs

- Create a Linux command notebook with 50 real commands and outputs.
- Host a simple page with Nginx or Python HTTP server and capture logs.
- Create a Git workflow lab: feature branch, PR, conflict, resolution, revert.

## Scenario-Based Interview Questions

1. A production Linux server is showing high CPU. What exact commands do you run first and what do you check before restarting anything?
2. A teammate pushed a bad commit to main. How do you recover without deleting history?
3. Users say the website is down but the app process is running. How do DNS, ports, firewall, and logs help you isolate the issue?
4. A file is readable locally but the service cannot read it. How do Linux user, group, permission, and SELinux/AppArmor possibilities change your debugging?
5. A pull request has merge conflicts. Explain how you resolve it and prove the final code is correct.

## Portfolio Proof

By the end of this track, learners should publish:

- One architecture diagram.
- One working lab or project.
- Screenshots or command logs.
- A troubleshooting note.
- Five written interview answers using the format: problem, architecture, decision, tradeoff, security, monitoring, rollback.

## Official References

- https://docs.github.com/en/get-started/using-git
- https://www.kernel.org/doc/html/latest/
- https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_happens_when_you_type_a_URL_in_the_address_bar
