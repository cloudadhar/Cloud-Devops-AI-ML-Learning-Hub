# Linux Commands and Practice

## Navigation

```bash
pwd
ls -la
cd /etc
find . -name "*.conf"
```

## Files

```bash
touch notes.txt
cp notes.txt backup.txt
mv backup.txt archive.txt
rm archive.txt
cat notes.txt
less notes.txt
head notes.txt
tail notes.txt
```

## Users and Permissions

```bash
whoami
id
sudo useradd learner
sudo passwd learner
chmod 640 file.txt
chown user:group file.txt
```

## Processes and Services

```bash
ps aux
top
systemctl status nginx
sudo systemctl restart nginx
journalctl -u nginx
```

## Networking

```bash
ip addr
ip route
ss -tulpn
curl -I https://example.com
```

## Practice Tasks

- Create a folder structure for a project.
- Create a user and assign file ownership.
- Install Nginx and serve a static page.
- Break Nginx config and recover from logs.
- Write a shell script that backs up a folder.

## References

- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [Nginx documentation](https://nginx.org/en/docs/)
