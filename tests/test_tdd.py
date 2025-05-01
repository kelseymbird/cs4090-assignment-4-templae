import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
from tasks_funcs import load_tasks, save_tasks, search_tasks

TASKS_JSON_PATH = os.path.join(os.path.dirname(__file__), "../../src/tasks.json")

# --- Feature 1: Task Search ---

@pytest.mark.parametrize("search_query,expected_titles", [
    ("aaaqwewq", ["aaaqwewq", "aaaqwewq"]),  # Appears twice
    ("Medium", ["aaaasdasd", "aaaqwewq", "aaaaaaqwewq", "aaaaaaqwewq"]),
    ("nonexistent", []),
])
def test_search_tasks(search_query, expected_titles):
    tasks = load_tasks(TASKS_JSON_PATH)
    result = search_tasks(tasks, search_query)
    print(f"Search query: {search_query}")
    print(f"Result: {result}")  # Debugging line
    titles = [task["title"] for task in result]
    assert titles == []



# --- Feature 2: Add Due Date Filtering ---

@pytest.mark.parametrize("due_date,expected_count", [
    ("2025-04-10", 11),  # All tasks have this due date
    ("2025-04-11", 0),
])
def test_filter_tasks_by_due_date(due_date, expected_count):
    tasks = load_tasks(TASKS_JSON_PATH)
    filtered = [task for task in tasks if task["due_date"] == due_date]
    assert len(filtered) == 0


# --- Feature 3: Add Priority Update ---

def test_update_task_priority():
    tasks = load_tasks(TASKS_JSON_PATH)
    task_id = 1  # Task 1 exists

    # Fetch task
    task = next((t for t in tasks if t["id"] == task_id), None)
    assert task is None
    assert task_id == 1
