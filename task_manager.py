import json
import sys
from pathlib import Path

# Path to the JSON file where tasks will be stored
TASK_FILE = Path("tasks.json")

# Load tasks from file
def load_tasks():
    if TASK_FILE.exists():
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add new task
def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {task_name}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} {status}")

# Mark a task as done
def mark_done(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("🎉 Task marked as done!")
    else:
        print("❌ Invalid task number")

# Delete a task
def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['task']}")
    else:
        print("❌ Invalid task number")

# Main command-line logic
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py [add|list|done|delete] [task]")
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) >= 3:
            add_task(sys.argv[2])
        elif command == "list":
            list_tasks()
        elif command == "done" and len(sys.argv) == 3:
            mark_done(int(sys.argv[2]))
        elif command == "delete" and len(sys.argv) == 3:
            delete_task(int(sys.argv[2]))
        else:
            print("Unknown command")
