# Lessons Learned: Interview Question Refinement

- **Handling Tool Blocks (e.g., reCAPTCHA):** When automated tools like `browser_action` are blocked, immediately inform the user and offer clear alternatives (manual input, alternative tools) rather than repeated attempts.
- **Improved Loop Detection & Error Handling for `apply_diff`:** Implement a retry limit for `apply_diff` operations. If a file modification fails repeatedly due to content mismatches, the agent should propose a full file rewrite or request the user to provide the complete, updated content. This prevents wasteful loops and improves efficiency.
- **Proactive Communication of Tool Limitations:** Clearly communicate the specific requirements of tools (e.g., `apply_diff` needing exact content matches) to the user or to internal planning, allowing for better strategic decisions (e.g., preferring full file rewrites for complex modifications).
