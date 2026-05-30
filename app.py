import os
from flask import Flask, request, jsonify, render_template
import requests
from agent import Agent
from agent.storage import SQLiteStorage


app = Flask(__name__)

storage = SQLiteStorage(db_path=os.environ.get("AGENT_DB", "agent.db"))
agent = Agent(name=os.environ.get("AGENT_NAME", "WebAgent"), storage=storage)

# Auth token (if set, endpoints require Authorization: Bearer <token>)
API_TOKEN = os.environ.get("AGENT_API_TOKEN")
# Outbound webhook URL (if set, agent will POST results)
WEBHOOK_URL = os.environ.get("AGENT_WEBHOOK_URL")


@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.get_json() or {}
    task = data.get("task")
    if not task:
        return jsonify({"error": "`task` required"}), 400
    # Auth check
    if API_TOKEN:
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer ") or auth.split()[1] != API_TOKEN:
            return jsonify({"error": "unauthorized"}), 401
    result = agent.run(task)

    # Send webhook if configured (best-effort)
    if WEBHOOK_URL:
        try:
            requests.post(WEBHOOK_URL, json={"task": task, "result": result}, timeout=5)
        except Exception:
            pass
    return jsonify({"result": result})


@app.route("/conversations")
def conversations():
    rows = agent.list_conversations(limit=100)
    convs = [
        {"id": r[0], "task": r[1], "response": r[2], "created_at": r[3]} for r in rows
    ]
    return render_template("conversations.html", conversations=convs)


@app.route("/api/conversations")
def api_conversations():
    rows = agent.list_conversations(limit=100)
    convs = [
        {"id": r[0], "task": r[1], "response": r[2], "created_at": r[3]} for r in rows
    ]
    return jsonify(convs)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/openapi.json")
def openapi_spec():
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "My AI Agent API", "version": "1.0.0"},
        "paths": {
            "/api/run": {
                "post": {
                    "summary": "Run a task",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {"schema": {"type": "object", "properties": {"task": {"type": "string"}}, "required": ["task"]}}
                        },
                    },
                    "responses": {"200": {"description": "OK"}, "400": {"description": "Bad Request"}},
                }
            }
        },
    }
    return jsonify(spec)


@app.route("/docs")
def docs_ui():
    return render_template("docs.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
