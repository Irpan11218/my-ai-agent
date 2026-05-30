import tempfile
from agent.agent import Agent
from agent.storage import SQLiteStorage


def test_agent_runs_and_saves():
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    db_path = tmp.name
    tmp.close()

    storage = SQLiteStorage(db_path=db_path)
    agent = Agent(name="TestAgent", storage=storage)

    res = agent.run("hello")
    assert "menjalankan tugas" in res

    rows = storage.list_conversations(10)
    assert len(rows) == 1
    assert rows[0][1] == "hello"
