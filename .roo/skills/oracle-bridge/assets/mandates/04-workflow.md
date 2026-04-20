# Mandate: The Oracle Workflow (EPIV)

This mandate defines the execution loop for all tasks.

## 1. The EPIV Loop
1. **Explore**: Systematically map the codebase and validate assumptions.
2. **Plan**: Define a strategy before implementation.
3. **Implement**: Apply targeted and idiomatic changes.
4. **Verify**: Provide empirical evidence (tests or logs) of success.

## 2. Decision Protocol
- **Directives**: Clear requests for action. Implement autonomously after planning.
- **Inquiries**: Requests for analysis. Provide findings without modifying files.
- **Ambiguity**: Seek clarification before proceeding.

## 3. The Verification Rule
A task is considered complete only when behavioral correctness has been demonstrated through a verifiable shell command (build, test, or lint log).
