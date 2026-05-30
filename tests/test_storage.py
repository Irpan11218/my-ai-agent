import tempfile
from agent.storage import SQLiteStorage


def test_storage_save_and_list():
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    db_path = tmp.name
    tmp.close()

    s = SQLiteStorage(db_path=db_path)
    s.save_conversation("t1", "r1")
    s.save_conversation("t2", "r2")

    rows = s.list_conversations(10)
    assert len(rows) == 2
    assert rows[0][1] in ("t2", "t1")
