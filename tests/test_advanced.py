import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))
from tasks_funcs import filter_tasks_by_priority, filter_tasks_by_category, generate_unique_id

# --- Fixtures ---

@pytest.fixture
def sample_tasks():
    return [
        {"id": 1, "title": "Task 1", "priority": "Low", "category": "Work"},
        {"id": 2, "title": "Task 2", "priority": "High", "category": "Personal"},
        {"id": 3, "title": "Task 3", "priority": "Medium", "category": "School"}
    ]

# --- Parameterized Tests ---

@pytest.mark.parametrize("priority,expected_count", [
    ("Low", 1),
    ("High", 1),
    ("Medium", 1),
    ("Urgent", 0),
])
def test_filter_tasks_by_priority_param(sample_tasks, priority, expected_count):
    filtered = filter_tasks_by_priority(sample_tasks, priority)
    assert len(filtered) == expected_count

@pytest.mark.parametrize("category,expected_titles", [
    ("Work", ["Task 1"]),
    ("Personal", ["Task 2"]),
    ("School", ["Task 3"]),
    ("Other", []),
])
def test_filter_tasks_by_category_param(sample_tasks, category, expected_titles):
    filtered = filter_tasks_by_category(sample_tasks, category)
    titles = [task["title"] for task in filtered]
    assert titles == expected_titles

# --- Mocking Example ---

def test_generate_unique_id_with_mock(mocker):
    mock_tasks = [{"id": 1}, {"id": 2}, {"id": 5}]
    mocker.patch("tasks_funcs.generate_unique_id", return_value=10)
    
    unique_id = generate_unique_id(mock_tasks)
    assert unique_id == 6 # because we mocked it!
