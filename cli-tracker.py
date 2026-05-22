import sys,os,json,datetime

class Task:
    def __init__(self,id,description):
        self.id = id
        self.description = description
        self.status = 'todo'
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

if len(sys.argv) < 2:
    print("Not a correct command")
    sys.exit(1)

operation = sys.argv[1]




def load_tasks(flag="all"):
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json",'r') as f:
        tasks = json.load(f)
        if flag == "all":
            return tasks
        filtered = [t for t in tasks if t["status"] == flag]
        return filtered          

def save_tasks(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=4)

#I found objects easier to organize. touche.
# __dict__ converts the Task instance to a plain Python dict
# json.dump then writes that dict to the file as a JSON string


def add_task(description):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks),default=0) + 1
    new_task = Task(new_id,description)
    tasks.append(new_task.__dict__)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(id:int,description:str):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == id:
            t["description"] = description
            t["updated_at"] = datetime.datetime.now().isoformat()
            break
    save_tasks(tasks)

def mark_task(id: int, status: str):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == id:
            t["status"] = status
            t["updated_at"] = datetime.datetime.now().isoformat()
            break
    save_tasks(tasks)

def delete_tasks(id:int):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            break
    save_tasks(tasks)
    print(f"Task {id} deleted successfully")

if operation == "list":
    if len(sys.argv) == 3:
        tasks = load_tasks(sys.argv[2])
    else:
        tasks = load_tasks()
    for t in tasks:
        print(f"[{t['id']}] {t['description']} - {t['status']}")

elif operation == "add":
    if len(sys.argv) < 3:
        print("Please provide a task description")
        sys.exit(1)
    add_task(sys.argv[2])

elif operation == "update":
    if len(sys.argv) < 4:
        print("Please provide task id and updated description")
        sys.exit(1)
    update_task(int(sys.argv[2]),sys.argv[3])

elif operation == "mark-in-progress":
    if len(sys.argv) < 3:
        print("Please provide a valid id")
        sys.exit(1)
    mark_task(int(sys.argv[2]), "in-progress")

elif operation == "mark-done":
    if len(sys.argv)<3:
        print("Please provide a valid id")
        sys.exit(1)
    mark_task(int(sys.argv[2]), "done")

elif operation == "delete":
    if len(sys.argv) < 3:
        print("Please Enter a Valid Id to delete.")
        sys.exit(1)
    delete_tasks(int(sys.argv[2]))
else:
    print(f"Unknown command: {operation}")
    sys.exit(1)
    
    