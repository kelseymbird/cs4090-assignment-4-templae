* test_advanced.py
The test_advanced.py file is designed to evaluate more 
complex functionality within the task management system, 
such as filtering by multiple criteria, task sorting, or 
integration logic involving several task attributes. The 
design choice here was to separate these multi-faceted 
test cases from basic unit tests to maintain clarity and 
modularity. This structure helps isolate edge cases and 
ensures that advanced behaviors work as expected without 
crowding simpler tests with intricate assertions or 
setups.

* test_basic.py
The test_basic.py file focuses on testing the core 
utilities and behaviors of the task system, such as 
loading and saving tasks, ID generation, and simple 
filtering operations. This file was designed with 
simplicity and accessibility in mind, serving as the 
foundation of the test suite. By concentrating on 
single-responsibility unit tests, this file allows 
developers to quickly verify that the fundamental 
building blocks of the application behave as intended, 
providing confidence before testing more complex 
functionality.

* test_property.py
In test_property.py, property-based testing is used to 
validate the robustness of the task system by checking 
how it handles a wide range of input values. The design 
choice to include this file stems from a desire to go 
beyond static test cases and dynamically generate inputs 
to uncover edge conditions or hidden bugs. This approach 
ensures that core methods, especially those involving 
filtering or transformations, can reliably handle 
unexpected or boundary-case input data.

* test_tdd.py
The test_tdd.py file reflects a test-driven development 
(TDD) approach, where tests are written prior to or 
alongside the development of new features. The design 
here is incremental: each test aligns with a feature or 
requirement that guided code implementation. This file 
serves both as documentation for development intent and 
a safety net for refactoring. It emphasizes behavior 
specification and often contains smaller, focused tests 
that evolve with the codebase.

* test_add_steps.py
The test_add_steps.py file is structured to test the 
step-by-step process of task creation in the UI, likely 
focusing on how user input is collected and how form 
data is processed. The design prioritizes simulating 
real user interactions, such as filling out forms or 
clicking buttons, and verifying that the backend state 
changes accordingly. This test file bridges the gap 
between frontend interaction and backend logic, ensuring 
that tasks are correctly instantiated and stored based 
on user inputs.