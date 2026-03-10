---
epoch: 1762328280602
modelKey: "gemini-2.5-flash|google"
topic: "AI API Errors"


tags:
  - copilot-conversation
---

**user**: explain the workflow of this knowledge system
[Timestamp: 2025/11/05 14:38:00]

**ai**: 
<errorChunk>Something went wrong. Please check if you have set your API key.
Path: Settings > copilot plugin > Basic Tab > Set Keys.
Or check model config
Error Details: 401 No cookie auth credentials found</errorChunk>
[Timestamp: 2025/11/05 14:38:01]

**user**: explain the workflow of this knowledge system

[Timestamp: 2025/11/05 14:39:35]

**ai**: 
<errorChunk>429 You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.

</errorChunk>
[Timestamp: 2025/11/05 14:39:36]

**user**: explain the workflow of this knowledge system

[Timestamp: 2025/11/05 14:44:56]

**ai**: This knowledge system processes information through four main stages: Capture, Review, Refine, and Curate [^1]. The lifecycle of a note is tracked using a `status` field, which can have the following values [^1]:

*   **raw**: The initial state for all new, unprocessed information captures.
*   **in-progress**: Indicates that the note is currently being worked on, refined, or tested.
*   **current**: Signifies that the note is validated, complete, and actively in use.
*   **archived**: Used for notes that are outdated, rejected, or no longer relevant.

The workflow begins with the **Capture** stage, which is the entry point for all raw information. All notes created in this stage are automatically assigned the `status: raw` [^2]. Examples of how information is captured include:

*   **Thoughts:** Become an `Idea.md` note [^2].
*   **Web Pages:** Become a `Web clipped.md` note [^2].
*   **Reports/Literature:** A source file (PDF) is saved, and a new `Literature Note.md` is created to track it [^2].
*   **Meetings:** Can result in an `Idea.md` or a `Task.md` note, with tasks initially set to `status: todo` [^2].

#### Sources
[^1]: [[_Meta/Workflow]]
[^2]: [[_Meta/Workflow]]
[Timestamp: 2025/11/05 14:45:16]