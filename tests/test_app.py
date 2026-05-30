import os
import importlib


def test_api_run_and_persistence(monkeypatch):
    # Set env to require token and a fake webhook
    os.environ['AGENT_API_TOKEN'] = 'testtoken'
    os.environ['AGENT_WEBHOOK_URL'] = 'http://example.com/hook'

    # Reload app so it picks up env vars
    import app as appmod
    importlib.reload(appmod)
    app = appmod.app

    called = {}

    def fake_post(url, json=None, timeout=None):
        called['url'] = url
        called['json'] = json
        class R:
            status_code = 200
        return R()

    monkeypatch.setattr('app.requests.post', fake_post)

    client = app.test_client()
    resp = client.post("/api/run", json={"task": "ping"}, headers={"Authorization": "Bearer testtoken"})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "result" in data

    # verify webhook called
    assert called.get('url') == 'http://example.com/hook'

    from agent.storage import SQLiteStorage
    s = SQLiteStorage(db_path=os.environ.get('AGENT_DB', 'agent.db'))
    rows = s.list_conversations(5)
    assert any(r[1] == "ping" for r in rows)
