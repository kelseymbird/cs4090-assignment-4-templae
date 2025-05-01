import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src")))
from tasks_funcs import load_tasks, save_tasks, generate_unique_id, filter_tasks_by_priority, filter_tasks_by_category
def test_load_tasks_empty(tmp_path):
    file_path = str(tmp_path / "tasks.json")  # <-- cast to str
    tasks = load_tasks(file_path)
    assert tasks == []

def test_save_and_load_tasks(tmp_path):
    file_path = str(tmp_path / "tasks.json")  # <-- cast to str
    data = [{"id": 1, "title": "Test Task", "completed": False}]
    save_tasks(data, file_path)
    loaded = load_tasks(file_path)
    assert loaded == data

def test_generate_unique_id_empty():
    tasks = []
    assert generate_unique_id(tasks) == 1

def test_generate_unique_id_existing():
    tasks = [{"id": 1}, {"id": 3}, {"id": 2}]
    assert generate_unique_id(tasks) == 4

def test_filter_tasks_by_priority():
    tasks = [
        {"title": "Task1", "priority": "High"},
        {"title": "Task2", "priority": "Low"}
    ]
    filtered = filter_tasks_by_priority(tasks, "High")
    assert len(filtered) == 1
    assert filtered[0]["priority"] == "High"

def test_filter_tasks_by_category():
    tasks = [
        {"title": "Task1", "category": "Work"},
        {"title": "Task2", "category": "Personal"}
    ]
    filtered = filter_tasks_by_category(tasks, "Work")
    assert len(filtered) == 1
    assert filtered[0]["category"] == "Work"
