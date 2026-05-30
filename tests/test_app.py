import json
from app import app
from agent.storage import SQLiteStorage


def test_api_run_and_persistence():
    client = app.test_client()
    resp = client.post("/api/run", json={"task": "ping"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "result" in data

    s = SQLiteStorage(db_path="agent.db")
    rows = s.list_conversations(5)
    assert any(r[1] == "ping" for r in rows)
