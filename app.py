from flask import Flask, request, jsonify, render_template
from agent import Agent
from agent.storage import SQLiteStorage


app = Flask(__name__)

storage = SQLiteStorage(db_path="agent.db")
agent = Agent(name="WebAgent", storage=storage)


@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.get_json() or {}
    task = data.get("task")
    if not task:
        return jsonify({"error": "`task` required"}), 400
    result = agent.run(task)
    return jsonify({"result": result})


@app.route("/conversations")
def conversations():
    rows = agent.list_conversations(limit=100)
    convs = [
        {"id": r[0], "task": r[1], "response": r[2], "created_at": r[3]} for r in rows
    ]
    return render_template("conversations.html", conversations=convs)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
