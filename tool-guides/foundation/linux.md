# Linux Zero to Hero Guide

## What It Is

Linux is the operating system foundation behind most servers, containers, Kubernetes nodes, cloud VMs, and DevOps automation environments.

## Why It Matters

- Helps learners understand where the tool fits in real engineering work.
- Connects theory with projects, interviews, and production troubleshooting.
- Gives a path from beginner usage to advanced integration.

## Short History

Linux began in 1991 when Linus Torvalds released the Linux kernel. Over time, Linux distributions such as Ubuntu, Debian, Red Hat, CentOS, Rocky Linux, and Amazon Linux became the backbone of internet infrastructure and cloud computing.

## Architecture and Core Concepts

Core architecture:

```text
User -> Shell -> System calls -> Linux kernel -> CPU / Memory / Disk / Network
```

Important concepts:

- Kernel, shell, filesystem, process, service, user, group, permission.
- Package managers such as apt, yum, dnf, and apk.
- Service managers such as systemd.
- Logs under `/var/log` and service logs through `journalctl`.
- Networking through interfaces, routes, DNS, ports, and firewalls.

## Zero to Hero Learning Path

1. Learn file navigation: pwd, ls, cd, find.
2. Learn file operations: cat, less, cp, mv, rm, touch.
3. Learn users, groups, chmod, chown, sudo.
4. Learn processes: ps, top, kill, systemctl.
5. Learn networking: ip, ss, curl, dig, nc.
6. Learn shell scripting and cron.
7. Learn log troubleshooting with journalctl and /var/log.
8. Run Nginx or Docker on Linux and debug failures.

## How to Start Using It

Start with a local Ubuntu VM, WSL, cloud VM, or container. Practice every command manually, then automate simple tasks with Bash scripts.

```bash
pwd
ls -la
cat /etc/os-release
ps aux
ss -tulpn
systemctl status nginx
journalctl -u nginx
```

## Common Integrations and Pipeline Usage

Linux is used in almost every DevOps pipeline:

```text
GitHub Actions runner -> Linux shell -> build scripts -> Docker -> Kubernetes node
```

It integrates with SSH, Docker, Kubernetes, Terraform provisioners, Ansible playbooks, Nginx, Prometheus exporters, and cloud VMs.

## Advanced Topics

- Systemd unit files and service hardening.
- Linux namespaces and cgroups for containers.
- Firewalls using ufw, firewalld, iptables, or nftables.
- Performance debugging using top, iostat, vmstat, sar, strace.
- Log rotation and audit logs.
- Linux security baselines and CIS hardening.

## Hands-on Project

Build a Linux troubleshooting notebook. Install Nginx, break its config, find the error from logs, fix it, and document the commands.

## Interview Questions

- What happens when a Linux service fails to start?
- Explain chmod 755 and chmod 640.
- How do you find which process is using a port?
- How do you check disk usage?
- How do you view logs for a systemd service?

## References

- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Linux Foundation Resources](https://www.linuxfoundation.org/resources/open-source-guides)
