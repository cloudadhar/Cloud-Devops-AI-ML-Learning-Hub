# CI/CD Pipeline Examples

## Basic Web App Pipeline

```text
checkout -> install -> lint -> test -> build -> package -> deploy
```

## DevSecOps Pipeline

```text
checkout -> secret scan -> lint -> test -> SAST -> dependency scan -> container build -> image scan -> IaC scan -> deploy -> smoke test
```

## MLOps Pipeline

```text
data validation -> train -> evaluate -> register model -> build serving image -> deploy -> monitor drift
```

## GitHub Actions Beginner Checklist

- Use least privilege permissions.
- Store secrets in GitHub Secrets.
- Cache dependencies carefully.
- Upload artifacts when useful.
- Fail fast on tests and scans.
- Keep deployment manual until learners understand cost and rollback.

## Interview Notes

Be ready to explain:

- What triggers the pipeline?
- What happens when a test fails?
- Where are artifacts stored?
- How are secrets protected?
- How do you roll back?
