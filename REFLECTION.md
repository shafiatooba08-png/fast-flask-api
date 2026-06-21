# Reflection: CI/CD Pipeline Fundamentals

### What does each stage of your pipeline protect against?
- **Lint Step:** Protects against code smell, bad formatting, stylistic inconsistencies, and basic syntax issues before the code even executes.
- **Test Step:** Protects against functional regressions, faulty logic, and broken application code by running automated integration and unit tests.
- **Deploy Step:** Protects against unauthorized deployment triggers (such as pulling experimental feature branches straight to production) and system-wide downtime.

### Why does the order matter — what could go wrong if deploy ran before test?
The order ensures that we only push *proven, reliable* artifacts into production. If the `deploy` stage executed before or concurrently with the `test` stage, syntax errors or broken logical regressions could be published live to end-users, leading to service disruption, database corruption, or user-facing bugs.

### What's one thing you'd add to make this pipeline closer to a real production setup?
To elevate this pipeline to a production standard, I would add a **Containerization & Secret Management** stage. Instead of merely echoing text, the deploy step would build a secure Docker container, push it to a secure cloud registry (like AWS ECR or Docker Hub), and trigger a rolling update hook on a cloud host using secrets securely stored within GitHub Actions.