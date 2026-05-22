# Task Tracker CLI

> This project is a part of the [roadmap.sh Task Tracker Project](https://roadmap.sh/projects/task-tracker)
>
> **Project URL:** https://roadmap.sh/projects/task-tracker
A simple command line app to track your tasks. Add tasks, update them, mark progress, and delete them , all stored in a local JSON file. 
---
## Requirements
- Python 3
---

## Setup
Clone or download the project, then navigate to the folder:

```bash
cd task-tracker
```

That's it. No installation required.

---

## Usage

Run all commands with:

```bash
python3 cli-tracker.py <command> [arguments]
```
---

## Commands

### Add a task

```bash
python3 cli-tracker.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### List all tasks

```bash
python3 cli-tracker.py list
```

### List tasks by status

```bash
python3 cli-tracker.py list todo
python3 cli-tracker.py list in-progress
python3 cli-tracker.py list done
```

### Update a task

```bash
python3 cli-tracker.py update 1 "Buy groceries and cook dinner"
```

### Mark a task as in progress

```bash
python3 cli-tracker.py mark-in-progress 1
```

### Mark a task as done

```bash
python3 cli-tracker.py mark-done 1
```

### Delete a task

```bash
python3 cli-tracker.py delete 1
```

---

## Task Properties

Each task stored in `tasks.json` has the following fields:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier |
| `description` | What the task is |
| `status` | `todo`, `in-progress`, or `done` |
| `created_at` | When the task was created |
| `updated_at` | When the task was last modified |

---

## Example Workflow

```bash
python3 cli-tracker.py add "Buy groceries"
python3 cli-tracker.py add "Cook dinner"
python3 cli-tracker.py mark-in-progress 1
python3 cli-tracker.py mark-done 1
python3 cli-tracker.py list done
python3 cli-tracker.py delete 2
```

---

## Data Storage

Tasks are saved in a `tasks.json` file in the same directory. The file is created automatically on the first run.
