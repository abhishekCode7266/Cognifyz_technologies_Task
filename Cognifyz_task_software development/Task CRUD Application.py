from datetime import datetime
class Task:
    def __init__(self, task_id, title, description, priority="Medium", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status1 
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self):
        title = input("Enter task title: ").strip()

        while not title:
            print("Title cannot be empty.")
            title = input("Enter task title: ").strip()

        description = input("Enter task description: ").strip()

        print("1. Low")
        print("2. Medium")
        print("3. High")

        choice = input("Select priority: ").strip()
        priority = {"1": "Low", "2": "Medium", "3": "High"}.get(choice, "Medium")

        task = Task(
            self.next_id,
            title,
            description,
            priority
        )

        self.tasks.append(task)
        print(f"Task created successfully. ID: {self.next_id}")

        self.next_id += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nID   Title                Priority   Status")
        print("-" * 50)

        for task in self.tasks:
            print(
                f"{task.task_id:<4}"
                f"{task.title[:20]:<21}"
                f"{task.priority:<11}"
                f"{task.status}"
            )

    def view_task(self):
        if not self.tasks:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Invalid task ID.")
            return

        task = self.find_task(task_id)

        if task:
            print("\nTask Details")
            print(f"ID: {task.task_id}")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Priority: {task.priority}")
            print(f"Status: {task.status}")
            print(f"Created: {task.created_at}")
        else:
            print("Task not found.")

    def update_task(self):
        if not self.tasks:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Invalid task ID.")
            return

        task = self.find_task(task_id)

        if not task:
            print("Task not found.")
            return

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

        print("Task updated successfully.")

    def delete_task(self):
        if not self.tasks:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid task ID.")
            return

        task = self.find_task(task_id)

        if not task:
            print("Task not found.")
            return

        confirm = input(
            f"Delete '{task.title}'? (y/n): "
        ).strip().lower()

        if confirm in ["y", "yes"]:
            self.tasks.remove(task)
            print("Task deleted successfully.")
        else:
            print("Delete cancelled.")

    def search_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        keyword = input("Enter keyword: ").strip().lower()

        results = [
            task for task in self.tasks
            if keyword in task.title.lower()
            or keyword in task.description.lower()
        ]

        if not results:
            print("No matching tasks found.")
            return

        for task in results:
            print(
                f"{task.task_id} - {task.title} - "
                f"{task.priority} - {task.status}"
            )

    def summary(self):
        total = len(self.tasks)
        completed = sum(
            task.status == "Completed"
            for task in self.tasks
        )
        in_progress = sum(
            task.status == "In Progress"
            for task in self.tasks
        )
        pending = sum(
            task.status == "Pending"
            for task in self.tasks
        )

        print("\nTask Summary")
        print(f"Total: {total}")
        print(f"Completed: {completed}")
        print(f"In Progress: {in_progress}")
        print(f"Pending: {pending}")

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task

        return None


def main():
    manager = TaskManager()

    while True:
        print("\nTASK MANAGEMENT SYSTEM")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. View Task Details")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Search Tasks")
        print("7. View Summary")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.create_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_task()
        elif choice == "4":
            manager.update_task()
        elif choice == "5":
            manager.delete_task()
        elif choice == "6":
            manager.search_tasks()
        elif choice == "7":
            manager.summary()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()