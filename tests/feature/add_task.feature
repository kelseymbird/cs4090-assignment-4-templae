Feature: Task Management

  Scenario: Adding a new task to the list
    Given I am on the task management page
    When I add a new task with title "Buy groceries", priority "High", category "Personal", and due date "2025-05-01"
    Then the task "Buy groceries" should appear in the task list

  Scenario: Marking a task as completed
    Given I have a task with title "Buy groceries" in the task list
    When I mark the task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  Scenario: Filtering tasks by category
    Given I have tasks in different categories
    When I filter tasks by category "Personal"
    Then I should see tasks with category "Personal"
    
  Scenario: Filtering tasks by priority
    Given I have tasks with different priorities
    When I filter tasks by priority "High"
    Then I should see tasks with priority "High"
