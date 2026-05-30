# my-ai-agent

[![CI](https://github.com/Irpan11218/my-ai-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/Irpan11218/my-ai-agent/actions)

Agent sederhana dengan CLI, API (Flask), dan penyimpanan SQLite.

Quick start:

```bash
python3 -m pip install -r requirements.txt
python3 app.py
```

CLI:

```bash
python3 cli.py --task "Halo"
```

Environment variables:
- `AGENT_API_TOKEN`: if set, API requires `Authorization: Bearer <token>` header.
- `AGENT_WEBHOOK_URL`: if set, agent will POST task/result to this URL after running.
- `AGENT_DB`: path to SQLite DB file (default `agent.db`).
