# Learning Method

Use the Learn, Build, Break, Fix, Explain method.

## 1. Learn

Read the concept from an official source. Write a short explanation in your own words.

Example:

- What is a reverse proxy?
- What problem does Nginx solve?
- Where does Kong fit compared with Nginx?

## 2. Build

Create a small working example.

Examples:

- Nginx serving a static page.
- Docker container running a Node.js API.
- Terraform creating one EC2 instance.
- GitHub Actions running tests.

## 3. Break

Change something intentionally and observe the failure.

Examples:

- Wrong port mapping.
- Missing environment variable.
- Bad Kubernetes image tag.
- Incorrect IAM permission.

## 4. Fix

Use logs, commands, and docs to solve it. Save the fix in [Troubleshooting Log Template](../logs/troubleshooting-log-template.md).

## 5. Explain

Explain the topic as if teaching a junior learner. If you cannot explain it, repeat the lab.

## Proof of Learning

Every topic should produce at least one of these:

- README note
- command sheet
- architecture diagram
- lab result screenshot
- pull request
- interview answer
- troubleshooting log
