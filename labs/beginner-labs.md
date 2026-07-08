# Beginner Labs

## Lab 1: Linux File and Permission Practice

Goal: understand files, folders, users, and permissions.

Tasks:

1. Create a project folder.
2. Create files using `touch`.
3. Change permissions with `chmod`.
4. Change ownership with `chown` if you have sudo access.
5. Explain the permission bits.

Cleanup:

```bash
rm -rf ~/linux-practice-demo
```

Interview questions:

- What does `chmod 640 file.txt` mean?
- How do you check file ownership?

## Lab 2: Git and GitHub Workflow

Goal: understand branch, commit, pull request, and merge.

Tasks:

1. Initialize a repo.
2. Create a branch.
3. Add a README.
4. Commit changes.
5. Push branch.
6. Open pull request.

Interview questions:

- What is a pull request?
- Merge vs rebase?

## Lab 3: Static Website with Nginx

Goal: serve a simple page using Nginx.

Tasks:

1. Install Nginx or run Nginx with Docker.
2. Replace the default page.
3. Use `curl` to test HTTP response.
4. Check access logs.

Interview questions:

- What is a web server?
- What is a reverse proxy?
