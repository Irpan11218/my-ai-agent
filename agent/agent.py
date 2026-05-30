class Agent:
    """Simple AI-like agent scaffold with optional storage.

    The agent can run simple tasks and persist conversations via a
    storage backend implementing `save_conversation(task, response)` and
    `list_conversations(limit)`.
    """
    def __init__(self, name: str = "MyAgent", storage: object | None = None):
        self.name = name
        self.storage = storage

    def run(self, task: str | None = None) -> str:
        """Execute a simple task and return a textual result.

        The current implementation echoes the task. If storage is provided,
        the conversation is saved.
        """
        if task:
            response = f"{self.name} menjalankan tugas: {task}"
            if self.storage:
                try:
                    self.storage.save_conversation(task, response)
                except Exception:
                    # Fail gracefully if storage errors
                    pass
            return response
        return f"{self.name} siap menerima tugas."

    def list_conversations(self, limit: int = 50):
        """Return stored conversations if storage is available."""
        if not self.storage:
            return []
        return self.storage.list_conversations(limit=limit)
