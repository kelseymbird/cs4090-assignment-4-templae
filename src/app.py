import streamlit as st
from datetime import datetime
import subprocess
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
from tasks_funcs import load_tasks, save_tasks, filter_tasks_by_priority, filter_tasks_by_category

# Function to run basic tests
def run_basic_tests():
    result = subprocess.run(["pytest", "test/test_basic.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("Basic tests passed!")
    else:
        st.error("Some basic tests failed. Check output above.")

# Function to run BDD tests
def run_bdd_tests():
    result = subprocess.run(["behave", "test/features"], capture_output=True, text=True)
    st.text(result.stdout)  # Display the output of the BDD tests
    if result.returncode == 0:
        st.success("BDD tests passed!")
    else:
        st.error("Some BDD tests failed. Check the output above.")

# Function to run Property-Based tests
def run_property_tests():
    result = subprocess.run(["pytest", "test/test_property.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("Property-based tests passed!")
    else:
        st.error("Some property-based tests failed. Check the output above.")
        
# Function to run Pytest with coverage reporting
def run_with_coverage():
    result = subprocess.run(["pytest", "--cov", "tasks", "test/test_basic.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("Tests passed with coverage!")
    else:
        st.error("Some tests failed. Check the output above.")

# Function to run parameterized tests
def run_parameterized_tests():
    result = subprocess.run(["pytest", "test/test_parameterized.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("Parameterized tests passed!")
    else:
        st.error("Some parameterized tests failed. Check the output above.")

# Function to run tests with mocking
def run_mocked_tests():
    result = subprocess.run(["pytest", "test/test_mocking.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("Mocking tests passed!")
    else:
        st.error("Some mocking tests failed. Check the output above.")

# Function to generate HTML report
def generate_html_report():
    result = subprocess.run(["pytest", "--html=report.html", "test/test_basic.py"], capture_output=True, text=True)
    st.text(result.stdout)
    if result.returncode == 0:
        st.success("HTML report generated successfully!")
    else:
        st.error("Failed to generate HTML report. Check the output above.")
        
# Main Streamlit app
def main():

    st.title("To-Do Application")
    
    # Load existing tasks
    tasks = load_tasks()  # Ensure tasks are loaded properly from storage

    # Sidebar for adding new tasks
    st.sidebar.header("Add New Task")
    with st.sidebar.form("new_task_form"):
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Description")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_category = st.selectbox("Category", ["Work", "Personal", "School", "Other"])
        task_due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Task")
        
        # Add the new task when the form is submitted
        if submit_button and task_title:
            new_task = {
                "id": len(tasks) + 1,  # Generate a unique ID for the task
                "title": task_title,
                "description": task_description,
                "priority": task_priority,
                "category": task_category,
                "due_date": task_due_date.strftime("%Y-%m-%d"),
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            tasks.append(new_task)
            save_tasks(tasks)
            st.sidebar.success("Task added successfully!")

    # Main area to display tasks
    st.header("Your Tasks")
    col1, col2 = st.columns(2)
    
    # Filters for tasks
    with col1:
        filter_category = st.selectbox("Filter by Category", ["All"] + list(set([task["category"] for task in tasks])))
    with col2:
        filter_priority = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])
    
    show_completed = st.checkbox("Show Completed Tasks")
    
    # Apply filters to tasks
    filtered_tasks = tasks.copy()
    if filter_category != "All":
        filtered_tasks = filter_tasks_by_category(filtered_tasks, filter_category)
    if filter_priority != "All":
        filtered_tasks = filter_tasks_by_priority(filtered_tasks, filter_priority)
    if not show_completed:
        filtered_tasks = [task for task in filtered_tasks if not task["completed"]]
    
    # Display tasks with actions
    for task in filtered_tasks:
        col1, col2 = st.columns([4, 1])
        with col1:
            if task["completed"]:
                st.markdown(f"~~**{task['title']}**~~")  # Strikethrough for completed tasks
            else:
                st.markdown(f"**{task['title']}**")
            st.write(task["description"])
            st.caption(f"Due: {task['due_date']} | Priority: {task['priority']} | Category: {task['category']}")
        with col2:
            # Button to mark task as completed or undo it
            if st.button("Complete" if not task["completed"] else "Undo", key=f"complete_{task['id']}"):
                for t in tasks:
                    if t["id"] == task["id"]:
                        t["completed"] = not t["completed"]
                        save_tasks(tasks)  # Save updated tasks list

                st.rerun()

            # Button to delete task
            if st.button("Delete", key=f"delete_{task['id']}"):
                tasks = [t for t in tasks if t["id"] != task["id"]]  # Remove the task
                save_tasks(tasks)  # Save updated tasks list
                st.rerun()

    # Buttons for tests
    if st.button("Run Basic Tests"):
        run_basic_tests()
        
    if st.button("Run BDD Tests"):
        run_bdd_tests()

    if st.button("Run Property-Based Tests"):
        run_property_tests()

    if st.button("Run Tests with Coverage"):
        run_with_coverage()

    if st.button("Run Parameterized Tests"):
        run_parameterized_tests()

    if st.button("Run Mocking Tests"):
        run_mocked_tests()

    if st.button("Generate HTML Report"):
        generate_html_report()

# Ensure tasks file and helper functions are properly set up
if __name__ == "__main__":
    main()
