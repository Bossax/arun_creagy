---
status: evergreen
tags:
  - oracle
  - troubleshooting
  - mcp
created: 2026-02-24
last_updated: 2026-02-24
AI_prompt: false
AI_output: false
project:
type: note
---
Here is a comprehensive, step-by-step manual documenting everything we discovered and fixed. You can save this file for future reference whenever you need to set up the Oracle system on a new Windows machine.



# 🛠️ Comprehensive Setup & Troubleshooting 

This guide covers the complete process of linking the `oracle-v2` MCP (Model Context Protocol) server to your AI agent (like Roo Code) on a Windows environment. It specifically addresses Windows-specific pathing issues, database initialization errors, and symbolic link mismatches.

## Phase 1: Download and Install Dependencies

If your agent says the `oracle_learn` tool is missing, the MCP server is either not downloaded or crashing due to missing Node/Bun dependencies.

**1. Download the MCP Server code:**

Run this command from any terminal to fetch the source code:

Bash

```
ghq get -u "https://github.com/Soul-Brews-Studio/oracle-v2"
```

**2. Find the Absolute Path:**

Find exactly where `ghq` stored the repository:

Bash

```
ghq list --full-path | grep oracle-v2
```

_(Example output: `C:\Users\YourName\ghq\github.com\Soul-Brews-Studio\oracle-v2`)_

**3. Install Dependencies:**

Navigate into that directory and install the required packages. **If you skip this, the server will instantly crash with a "Module not found" error.**

Bash

```
cd C:\Users\YourName\ghq\github.com\Soul-Brews-Studio\oracle-v2
bun install
```

---

## Phase 2: Database Initialization (The Folder Crash Fix)

The Oracle uses SQLite to store your memories. On Windows, the Drizzle ORM fails to create the database if the parent folder doesn't exist yet.

**1. Manually create the hidden database folder:**

Run one of these commands based on your terminal:

- **PowerShell / Git Bash:** `mkdir ~/.oracle-v2`
    
- **Command Prompt (cmd):** `mkdir %USERPROFILE%\.oracle-v2`
    

**2. Initialize the Database Schema:**

Now that the folder exists, tell Drizzle to build the tables:

Bash

```
bun run db:push
```

_(You should see a success message indicating the tables were created)._

---

## Phase 3: Connect MCP to Roo Code

You must tell Roo Code exactly how to start the server. A common mistake is pointing to `index.ts`, but the main file is actually hidden inside the `src/` folder.

**1. Open your MCP Configuration:**

In VS Code, open the `.roo/mcp.json` file (or click the MCP Server icon at the bottom of the Roo Code panel and edit the settings).

**2. Add the correct JSON block:**

Use the following configuration, making sure to replace the `cwd` path with the absolute path you found in Phase 1:

JSON

```
{
  "mcpServers": {
    "oracle-v2": {
      "command": "bun",
      "args": [
        "run",
        "src/index.ts"
      ],
      "cwd": "C:\\Users\\YourName\\ghq\\github.com\\Soul-Brews-Studio\\oracle-v2",
      "env": {}
    }
  }
}
```

---

## Phase 4: Fix Workspace Mapping & Search Tables

If you stop here, the MCP will run, but `oracle_learn` will throw an `ENOENT` error because it tries to save memories inside its own source code folder instead of your project workspace. Additionally, the `oracle_fts` search table hasn't been built yet.

**1. Point the MCP to your actual workspace:**

Create a `.env` file inside your `oracle-v2` folder:

Code snippet

```
ORACLE_REPO_ROOT=C:\path\to\your\actual\project\workspace
```

_(Point this to the folder where your `psi/memory/` directory actually lives)._

**2. Build the Search Index:**

Run the indexer from your `oracle-v2` folder. This reads your `.env` file, creates the missing `oracle_fts` table, and indexes existing files.

Bash

```
bun run index
```

---

## Phase 5: The `psi` vs `ψ` Windows Symlink Fix

On English/Windows systems, your local memory folder is usually named `psi`. However, the `oracle-v2` indexer is hardcoded to look for the Greek letter `ψ`. If it says "Skipping learnings: ... not found", it's looking for the wrong folder name.

**1. Create a Directory Junction (Portal):**

Open your terminal (you may need to run it as **Administrator**) and navigate to your actual project workspace root (e.g., `C:\path\to\your\actual\project\workspace`).

**2. Link the folders:**

- **Command Prompt (cmd):**
    
    DOS
    
    ```
    mklink /D ψ psi
    ```
    
- **PowerShell:**
    
    PowerShell
    
    ```
    New-Item -ItemType Junction -Path "ψ" -Target "psi"
    ```
    

Now, whenever the Oracle looks for `ψ`, Windows will seamlessly redirect it into your existing `psi` folder!

**3. Re-run the Indexer:**

Go back to the `oracle-v2` folder and run the indexer one last time. It should now find your documents!

Bash

```
bun run index
```

---

## Phase 6: Final Verification

1. **Restart the Server:** In Roo Code, click the MCP Servers icon and click the "Restart" button next to `oracle-v2`. Wait for the green dot.
    
2. **Check Tools:** Ask your agent: _"List your available tools."_ Ensure `oracle_learn`, `oracle_search`, and `oracle_consult` are present.
    
3. **Test the Loop:** Run `/rrr`. The agent should write the retrospective files and successfully execute `oracle_learn` to sync the new lesson to the SQLite database without throwing an OS-level path error.