# Arun_Creagy

A place for Arun Creagy Oracle.

## Local OpenAI Chat UI

This repository includes a minimal local web UI and Node/Express server that proxies chat requests to the OpenAI API.

### Files

- [server.js](server.js) – Express server with `/chat` endpoint, CORS, and static file serving from `public/`.
- [public/index.html](public/index.html) – Single-file HTML chat UI (no framework).

### Requirements

- Node.js 18+ installed locally.
- `OPENAI_API_KEY` set in your environment.

On macOS/Linux:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

On Windows PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-api-key-here"
```

### Install dependencies

```bash
npm install
```

### Run the server

```bash
node server.js
```

Then open http://localhost:3000 in your browser to use the chat UI.

