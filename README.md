# my-ai-agent

[![CI](https://github.com/Irpan11218/my-ai-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/Irpan11218/my-ai-agent/actions)
[![Image CI](https://github.com/Irpan11218/my-ai-agent/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Irpan11218/my-ai-agent/actions/workflows/docker-publish.yml)

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

Docker (recommended)
--------------------

Build image and run with docker-compose:

```bash
docker compose build
docker compose up -d
```

The web UI will be available at `http://localhost:5000` and the SQLite DB is persisted in the `data` volume.

To stop and remove containers:

```bash
docker compose down
```

Environment variables:
- `AGENT_API_TOKEN`: if set, API requires `Authorization: Bearer <token>` header.
- `AGENT_WEBHOOK_URL`: if set, agent will POST task/result to this URL after running.
- `AGENT_DB`: path to SQLite DB file (default `agent.db`).
