import os
from datetime import datetime

FILE_NAME = "tasks.txt"
class Task:
    def __init__(
        self,
        task_id,
        title,
        description,
        priority="Medium",
        status="Pending",
        due_date="N/A",
        created_at=None
    ):
        self.task_id = int(task_id)
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.created_at = created_at or datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

    def to_file_format(self):
        title = self.title.replace("|", "-")
        description = self.description.replace("|", "-")

        return (
            f"{self.task_id}|{title}|{description}|"
            f"{self.priority}|{self.status}|{self.due_date}|"
            f"{self.created_at}\n"
        )

    @classmethod
    def from_file_format(cls, line):
        parts = line.strip().split("|")

        if len(parts) == 7:
            return cls(
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4],
                parts[5],
                parts[6]
            )

        return None


tasks = []


def load_tasks():
    tasks.clear()

    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    task = Task.from_file_format(line)

                    if task:
                        tasks.append(task)

    except (OSError, ValueError) as error:
        print(f"Error loading tasks: {error}")


def save_tasks():
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task.to_file_format())

        return True

    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False


def get_next_id():
    if not tasks:
        return 1

    return max(task.task_id for task in tasks) + 1


def create_task():
    title = input("Enter task title: ").strip()

    while not title:
        print("Title cannot be empty.")
        title = input("Enter task title: ").strip()

    description = input("Enter task description: ").strip()

    print("1. Low")
    print("2. Medium")
    print("3. High")

    choice = input("Select priority: ").strip()

    priority = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }.get(choice, "Medium")

    due_date = input("Enter due date: ").strip()

    if not due_date:
        due_date = "N/A"

    task = Task(
        get_next_id(),
        title,
        description,
        priority,
        "Pending",
        due_date
    )

    tasks.append(task)
    save_tasks()

    print(f"Task created successfully. ID: {task.task_id}")


def read_tasks(task_list=None):
    records = tasks if task_list is None else task_list

    if not records:
        print("No tasks available.")
        return False

    print("\nID   Title                Priority   Status       Due Date")
    print("-" * 65)

    for task in records:
        print(
            f"{task.task_id:<5}"
            f"{task.title[:20]:<21}"
            f"{task.priority:<11}"
            f"{task.status:<13}"
            f"{task.due_date}"
        )

    return True


def view_task_details():
    if not read_tasks():
        return

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task.task_id == task_id:
            print("\nTask Details")
            print(f"ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority}")
            print(f"Status: {task.status}")
            print(f"Due Date: {task.due_date}")
            print(f"Created: {task.created_at}")
            return

    print("Task not found.")


def update_task():
    if not read_tasks():
        return

    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task.task_id == task_id:

            title = input(f"New title [{task.title}]: ").strip()

            if title:
                task.title = title

            description = input(
                f"New description [{task.description}]: "
            ).strip()

            if description:
                task.description = description

            print("1. Low")
            print("2. Medium")
            print("3. High")

            priority = input("Select priority: ").strip()

            if priority in ["1", "2", "3"]:
                task.priority = {
                    "1": "Low",
                    "2": "Medium",
                    "3": "High"
                }[priority]

            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")

            status = input("Select status: ").strip()

            if status in ["1", "2", "3"]:
                task.status = {
                    "1": "Pending",
                    "2": "In Progress",
                    "3": "Completed"
                }[status]

            due_date = input(
                f"New due date [{task.due_date}]: "
            ).strip()

            if due_date:
                task.due_date = due_date

            save_tasks()
            print("Task updated successfully.")
            return

    print("Task not found.")


def delete_task():
    if not read_tasks():
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid task ID.")
        return

    for task in tasks:
        if task.task_id == task_id:

            confirm = input(
                f"Delete '{task.title}'? (y/n): "
            ).strip().lower()

            if confirm in ["y", "yes"]:
                tasks.remove(task)
                save_tasks()
                print("Task deleted successfully.")
            else:
                print("Delete cancelled.")

            return

    print("Task not found.")


def search_tasks():
    if not tasks:
        print("No tasks available.")
        return

    keyword = input("Enter search term: ").strip().lower()

    results = [
        task for task in tasks
        if keyword in task.title.lower()
        or keyword in task.description.lower()
    ]

    read_tasks(results)


def show_statistics():
    total = len(tasks)
    completed = sum(
        task.status == "Completed"
        for task in tasks
    )
    in_progress = sum(
        task.status == "In Progress"
        for task in tasks
    )
    pending = sum(
        task.status == "Pending"
        for task in tasks
    )

    print("\nTask Summary")
    print(f"Total: {total}")
    print(f"Completed: {completed}")
    print(f"In Progress: {in_progress}")
    print(f"Pending: {pending}")


def create_backup():
    if not os.path.exists(FILE_NAME):
        print("No task file found.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"tasks_backup_{timestamp}.txt"

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as source:
            with open(backup_file, "w", encoding="utf-8") as backup:
                backup.write(source.read())

        print(f"Backup created: {backup_file}")

    except OSError as error:
        print(f"Backup failed: {error}")


def main():
    load_tasks()

    while True:
        print("\nTASK MANAGEMENT SYSTEM")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Search Tasks")
        print("7. View Summary")
        print("8. Create Backup")
        print("9. Reload Tasks")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_task()
        elif choice == "2":
            read_tasks()
        elif choice == "3":
            view_task_details()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            search_tasks()
        elif choice == "7":
            show_statistics()
        elif choice == "8":
            create_backup()
        elif choice == "9":
            load_tasks()
            print("Tasks reloaded.")
        elif choice == "10":
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()