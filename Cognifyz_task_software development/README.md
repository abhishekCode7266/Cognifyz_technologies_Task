# Task CRUD Application

A simple command-line Task Management System built with Python that allows users to create, read, update, and delete tasks with priority levels and status tracking.

## Features

- **Create Task**: Add new tasks with title, description, and priority level
- **View All Tasks**: Display all tasks in a formatted table
- **View Task Details**: Get detailed information about a specific task
- **Update Task**: Modify task details including title, description, priority, and status
- **Delete Task**: Remove tasks with confirmation
- **Search Tasks**: Find tasks by keyword in title or description
- **View Summary**: Get statistics on task completion and status

## Requirements

- Python 3.x
- No external dependencies required (uses only built-in Python modules)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/abhishekCode7266/Cognifyz_technologies_Task.git
cd Cognifyz_technologies_Task
```

2. Navigate to the application directory:
```bash
cd "Cognifyz_task_software development"
```

## Usage

Run the application:
```bash
python "Task CRUD Application.py"
```

### Main Menu Options

```
1. Create Task       - Add a new task to the system
2. View All Tasks    - Display all tasks in table format
3. View Task Details - View complete information for a specific task
4. Update Task       - Modify an existing task
5. Delete Task       - Remove a task from the system
6. Search Tasks      - Find tasks by keyword
7. View Summary      - Display task statistics
8. Exit              - Close the application
```

## How to Use

### Creating a Task
1. Select option `1` from the main menu
2. Enter task title (required)
3. Enter task description
4. Select priority level:
   - 1: Low
   - 2: Medium (default)
   - 3: High
5. Task is created with "Pending" status automatically

### Viewing Tasks
- **Option 2**: View all tasks in a condensed table format
- **Option 3**: Select a specific task ID to view its complete details including:
  - Task ID
  - Title
  - Description
  - Priority
  - Status
  - Creation timestamp

### Updating a Task
1. Select option `4`
2. View available tasks and enter the task ID to update
3. Update fields (press Enter to skip):
   - Title
   - Description
   - Priority level
   - Status:
     - 1: Pending
     - 2: In Progress
     - 3: Completed

### Deleting a Task
1. Select option `5`
2. View available tasks and enter the task ID
3. Confirm deletion with "y" or "n"

### Searching Tasks
1. Select option `6`
2. Enter a keyword to search in task titles and descriptions
3. View matching results

### Viewing Summary
1. Select option `7`
2. View statistics:
   - Total number of tasks
   - Completed tasks
   - Tasks in progress
   - Pending tasks

## Task Structure

Each task contains:
- **Task ID**: Unique identifier (auto-incremented)
- **Title**: Task name (required, non-empty)
- **Description**: Detailed task information
- **Priority**: Low, Medium, or High
- **Status**: Pending, In Progress, or Completed
- **Created At**: Timestamp of task creation (YYYY-MM-DD HH:MM format)

## Priority Levels

- **Low**: Non-urgent tasks
- **Medium**: Standard priority (default)
- **High**: Urgent tasks

## Status Levels

- **Pending**: Task not yet started
- **In Progress**: Task is being worked on
- **Completed**: Task is finished

## Example Workflow

```
1. Create a task titled "Complete project documentation"
   - Description: "Write comprehensive documentation for the API"
   - Priority: High
   
2. View all tasks to see the newly created task

3. Update the task status to "In Progress"

4. Search for tasks with keyword "documentation"

5. View summary to track progress

6. Mark as "Completed" when done
```

## Notes

- All tasks are stored in memory (data is lost when application closes)
- Task IDs are automatically generated and incremented
- Empty titles are not allowed during task creation
- Search is case-insensitive
- All timestamps are in `YYYY-MM-DD HH:MM` format

## Future Enhancements

- Persistent data storage (database or file)
- Due date functionality
- Task categories or tags
- Priority filtering
- Export tasks to CSV/JSON
- User authentication

## Author

Created by abhishekCode7266 for Cognifyz Technologies

## License

This project is part of Cognifyz Technologies Task assignment.

## Support

For issues or questions, please open an issue in the repository.
