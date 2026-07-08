# Linux Guide

## Topics

- Filesystem hierarchy
- Users and groups
- Permissions
- Processes
- Services and systemd
- Packages
- Shell scripting
- Networking commands
- Disk usage
- Logs
- SSH
- Cron

## Commands to Practice

```bash
pwd
ls -la
cd /var/log
cat /etc/os-release
grep -R "error" /var/log
ps aux
top
df -h
du -sh *
chmod
chown
systemctl status nginx
journalctl -u nginx
ssh user@server
scp file user@server:/tmp/
crontab -e
```

## Labs

- Create users and groups.
- Set file permissions.
- Install and manage Nginx.
- Write a backup shell script.
- Debug a failed service.
- Rotate and inspect logs.
