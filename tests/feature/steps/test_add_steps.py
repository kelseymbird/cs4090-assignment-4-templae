from behave import given, when, then
from tasks import load_tasks, save_tasks, generate_unique_id
import streamlit as st

# Initialize task list in a mock way
TASKS = load_tasks("tasks.json")

@given("I am on the task management page")
def step_impl(context):
    # Simulate loading the task management page in Streamlit
    context.tasks = TASKS

@when('I add a new task with title "{title}", priority "{priority}", category "{category}", and due date "{due_date}"')
def step_impl(context, title, priority, category, due_date):
    task_id = generate_unique_id(context.tasks)
    new_task = {
        "id": task_id,
        "title": title,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed": False,
        "created_at": "2025-04-27 10:00:00"
    }
    context.tasks.append(new_task)
    save_tasks(context.tasks)

@then('the task "{title}" should appear in the task list')
def step_impl(context, title):
    task_titles = [task["title"] for task in context.tasks]
    assert title in task_titles

@given('I have a task with title "{title}" in the task list')
def step_impl(context, title):
    context.task = {
        "id": generate_unique_id(context.tasks),
        "title": title,
        "priority": "Low",
        "category": "Work",
        "due_date": "2025-05-01",
        "completed": False,
        "created_at": "2025-04-27 10:00:00"
    }
    context.tasks.append(context.task)
    save_tasks(context.tasks)

@when('I mark the task "{title}" as completed')
def step_impl(context, title):
    for task in context.tasks:
        if task["title"] == title:
            task["completed"] = True
            save_tasks(context.tasks)

@then('the task "{title}" should be marked as completed')
def step_impl(context, title):
    for task in context.tasks:
        if task["title"] == title:
            assert task["completed"] is True

@given("I have tasks in different categories")
def step_impl(context):
    context.tasks = [
        {"id": 1, "title": "Buy groceries", "priority": "High", "category": "Personal", "due_date": "2025-05-01", "completed": False},
        {"id": 2, "title": "Work on project", "priority": "Medium", "category": "Work", "due_date": "2025-05-02", "completed": False},
        {"id": 3, "title": "Study for exam", "priority": "Low", "category": "School", "due_date": "2025-05-03", "completed": False}
    ]
    save_tasks(context.tasks)

@when('I filter tasks by category "{category}"')
def step_impl(context, category):
    context.filtered_tasks = [task for task in context.tasks if task["category"] == category]

@then('I should see tasks with category "{category}"')
def step_impl(context, category):
    for task in context.filtered_tasks:
        assert task["category"] == category

@given("I have tasks with different priorities")
def step_impl(context):
    context.tasks = [
        {"id": 1, "title": "Task 1", "priority": "High", "category": "Work", "due_date": "2025-05-01", "completed": False},
        {"id": 2, "title": "Task 2", "priority": "Low", "category": "Work", "due_date": "2025-05-02", "completed": False},
        {"id": 3, "title": "Task 3", "priority": "Medium", "category": "School", "due_date": "2025-05-03", "completed": False}
    ]
    save_tasks(context.tasks)

@when('I filter tasks by priority "{priority}"')
def step_impl(context, priority):
    context.filtered_tasks = [task for task in context.tasks if task["priority"] == priority]

@then('I should see tasks with priority "{priority}"')
def step_impl(context, priority):
    for task in context.filtered_tasks:
        assert task["priority"] == priority
