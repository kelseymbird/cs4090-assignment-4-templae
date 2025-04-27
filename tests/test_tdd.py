import pytest
from tasks import load_tasks, save_tasks

# --- Feature 1: Task Search ---

@pytest.mark.parametrize("search_query,expected_titles", [
    ("task 1", ["Task 1"]),
    ("medium", ["Task 3"]),
    ("nonexistent", []),
])
def test_search_tasks(search_query, expected_titles):
    tasks = load_tasks("tasks.json")  # Assuming tasks.json has these tasks
    result = search_tasks(tasks, search_query)
    titles = [task["title"] for task in result]
    assert titles == expected_titles


# --- Feature 2: Add Due Date Filtering ---

@pytest.mark.parametrize("due_date,expected_count", [
    ("2025-04-10", 3),
    ("2025-04-11", 0),
])
def test_filter_tasks_by_due_date(due_date, expected_count):
    tasks = load_tasks("tasks.json")  # Assuming tasks.json contains the task data
    filtered = [task for task in tasks if task["due_date"] == due_date]
    assert len(filtered) == expected_count


# --- Feature 3: Add Priority Update ---

def test_update_task_priority():
    tasks = load_tasks("tasks.json")
    task_id = 1  # We know Task 1 exists

    # Initial state check
    task = next(t for t in tasks if t["id"] == task_id)
    assert task["priority"] == "Low"

    # Change the priority
    task["priority"] = "High"
    save_tasks(tasks)  # Save to file after update

    # Verify the change
    task = next(t for t in tasks if t["id"] == task_id)
    assert task["priority"] == "High"
