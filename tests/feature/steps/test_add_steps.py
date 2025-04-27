from pytest_bdd import given, when, then, scenarios
from tasks import load_tasks, save_tasks, generate_unique_id

# Initialize task list in a mock way
TASKS = load_tasks("tasks.json")

scenarios('../features/add_task.feature')  # Import the feature file

@given("I am on the task management page")
def on_task_management_page():
    return TASKS

@when('I add a new task with title "{title}", priority "{priority}", category "{category}", and due date "{due_date}"')
def add_task(on_task_management_page, title, priority, category, due_date):
    task_id = generate_unique_id(on_task_management_page)
    new_task = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed": False,
        "created_at": "2025-04-27 10:00:00"
    }
    on_task_management_page.append(new_task)
    save_tasks(on_task_management_page)

@then('the task "{title}" should appear in the task list')
def task_should_appear_in_task_list(on_task_management_page, title):
    task_titles = [task["title"] for task in on_task_management_page]
    assert title in task_titles

@given('I have a task with title "{title}" in the task list')
def task_in_task_list(on_task_management_page, title):
    task = {
        "id": generate_unique_id(on_task_management_page),
        "title": title,
        "priority": "Low",
        "category": "Work",
        "due_date": "2025-05-01",
        "completed": False,
        "created_at": "2025-04-27 10:00:00"
    }
    on_task_management_page.append(task)
    save_tasks(on_task_management_page)

@when('I mark the task "{title}" as completed')
def mark_task_completed(on_task_management_page, title):
    for task in on_task_management_page:
        if task["title"] == title:
            task["completed"] = True
            save_tasks(on_task_management_page)

@then('the task "{title}" should be marked as completed')
def task_should_be_completed(on_task_management_page, title):
    for task in on_task_management_page:
        if task["title"] == title:
            assert task["completed"] is True
