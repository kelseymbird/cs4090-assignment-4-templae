from hypothesis import given, strategies as st
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))
from tasks_funcs import filter_tasks_by_priority, filter_tasks_by_category
import tasks_funcs

# --- Property Test 1: Filter tasks by priority with various inputs ---

@given(st.lists(st.dictionaries(keys=st.text(), values=st.integers())), st.sampled_from(["Low", "Medium", "High"]))
def test_filter_tasks_by_priority_property(tasks_list, priority):
    tasks_list = [
        {"id": 1, "title": "Task 1", "priority": priority, "category": "Work", "due_date": "2025-04-10", "completed": False},
        {"id": 2, "title": "Task 2", "priority": "Low", "category": "Work", "due_date": "2025-04-10", "completed": False}
    ]
    filtered = filter_tasks_by_priority(tasks_list, priority)
    assert all(task["priority"] == priority for task in filtered)


# --- Property Test 2: Filter tasks by category with various inputs ---

@given(st.lists(st.dictionaries(keys=st.text(), values=st.integers())), st.sampled_from(["Work", "School", "Personal", "Other"]))
def test_filter_tasks_by_category_property(tasks_list, category):
    tasks_list = [
        {"id": 1, "title": "Task 1", "priority": "Low", "category": category, "due_date": "2025-04-10", "completed": False},
        {"id": 2, "title": "Task 2", "priority": "Medium", "category": "Personal", "due_date": "2025-04-10", "completed": False}
    ]
    filtered = filter_tasks_by_category(tasks_list, category)
    assert all(task["category"] == category for task in filtered)

# --- Property Test 3: Unique Task ID generation ---

@given(st.lists(st.dictionaries(keys=st.just("id"), values=st.integers(), min_size=1)))
def test_generate_unique_id_property(tasks_list):
    new_id = tasks_funcs.generate_unique_id(tasks_list)
    
    existing_ids = [task["id"] for task in tasks_list]
    if existing_ids:
        assert new_id > max(existing_ids)
    else:
        assert new_id == 1