#!/usr/bin/env python3
"""Simple CLI to run the Agent."""
import argparse
from agent import Agent
from agent.storage import SQLiteStorage


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple agent CLI")
    parser.add_argument("--name", "-n", default="MyAgent", help="Nama agent")
    parser.add_argument("--task", "-t", help="Tugas yang diberikan ke agent")
    args = parser.parse_args()

    storage = SQLiteStorage(db_path="agent.db")
    agent = Agent(name=args.name, storage=storage)
    result = agent.run(task=args.task)
    print(result)


if __name__ == "__main__":
    main()
