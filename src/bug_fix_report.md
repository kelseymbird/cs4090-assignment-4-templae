Bug Report — To-Do Application (app.py)
Author: Kelsey Bird
Date: April 28, 2025

Application: To-Do Application
File Under Review: app.py
Language/Framework: Python 3.12, Streamlit

Description: A Streamlit-based task management tool allowing task creation, filtering, completion toggling, and deletion.

* Functional Bugs
1. Duplicate Task IDs on Deletion

Description: Task IDs are generated using len(tasks) + 1. This does not account for tasks that have been deleted.

Impact: This may result in duplicate task IDs, leading to incorrect behavior when toggling or deleting tasks.

Solution: Replace with a call to a reliable ID generation function such as generate_unique_id(tasks) or use a UUID generator.

2. load_tasks() and save_tasks() Used Without Arguments

Description: These functions are used with no parameters, but they likely expect a file path argument.

Impact: May raise a TypeError or fail silently depending on the implementation.

Solution: Pass the correct path explicitly, for example: load_tasks("tasks.json").

* User Experience and Logic Issues
3. No Feedback When Task Title Is Missing

Description: If the task form is submitted without a title, nothing is added and no message is shown.

Impact: This creates a confusing user experience.

Solution: Add a message like st.sidebar.warning("Task title is required") when the title field is empty.

4. Tasks Are Not Sorted by Due Date

Description: Tasks are shown in the order they were added, without sorting.

Impact: This makes it harder to prioritize or view tasks efficiently.

Solution: Add sorting using something like filtered_tasks.sort(key=lambda x: x["due_date"]).

* Data Integrity and State Handling
5. State Changes on Filtered Task List Modify the Main Task List

Description: The application performs completion toggles and deletions based on the filtered list but applies changes directly to the main list.

Impact: May cause unexpected behavior or race conditions.

Solution: Ensure that updates are based on direct access to the full list using unique IDs, not the filtered subset.

6. No Handling for Invalid or Malformed Dates

Description: All due dates are formatted with .strftime(), assuming that they are valid date objects.

Impact: If the date format is corrupted or inconsistent in storage, this may lead to runtime exceptions.

Solution: Implement error handling using try/except blocks or validate the input format during parsing.

7. Rerun for completed and deleted tasks

Description: The completion and deletion buttons didn't automatically reload the page, so it didn't look like the task had been delete though it had been

Impact: confusing the user

Solution: use 'st.rerun()' after each of the buttons is pressed to reload the page.