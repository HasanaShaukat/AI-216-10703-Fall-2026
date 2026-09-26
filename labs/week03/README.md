# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

## Concepts Practiced

* Functions
* Scope
* Modules and imports
* `__name__ == "__main__"`
* Exception handling
* Debugging
* Classes and objects
* Refactoring

## Tasks Completed

1. Function Design
2. Scope
3. Modules
4. Exception Handling
5. Debugging Challenge
6. ScoreAnalyzer Class
7. Refactoring Task

## Debugging Notes

### Bug Found

The first bug was in the `calculate_average` function.

The program was assigning each score to `total` instead of adding the scores together.

### How I Located It

I ran the program and checked the value of the average.

Then I manually traced the values of `total` inside the loop.

### How I Fixed It

I changed the assignment operation to an addition operation.

The second issue was in the `classify` function.

The Excellent condition needed to be checked before the Pass condition because 85 and above should be classified as Excellent.

### Debugging Output

Expected Output:

Average: 75.0
Result: Pass

Actual Output Before Fix:

Average: 22.5
Result: Fail

Actual Output After Fix:

Average: 75.0
Result: Pass

## Exception Handling Test Cases

| Case    | Input      | Expected Result | Actual Result |
| ------- | ---------- | --------------- | ------------- |
| Valid   | 80, 100    | 80%             | 80%           |
| Invalid | -5, 100    | Error           | Error         |
| Invalid | 120, 100   | Error           | Error         |
| Invalid | 80, 0      | Error           | Error         |
| Invalid | Text input | Error           | Error         |

### Actual Results

* 80, 100 → 80%
* -5, 100 → Error: Obtained marks cannot be negative.
* 120, 100 → Error: Obtained marks cannot be greater than total marks.
* 80, 0 → Error: Total marks must be greater than zero.
* Text input → Error: Please enter numeric values.

## Design Decisions

### Why did I use functions?

Functions are useful when a task can be reused and does not need to store persistent state.

### Why did I use a class?

A class is useful when data and related behavior need to stay together.

### What logic belongs in main.py?

`main.py` should coordinate the program flow and call functions or classes instead of containing all detailed logic.

## What I Found Difficult

Debugging the incorrect average calculation and understanding the order of conditions were difficult.

## What I Learned

I learned how to create reusable functions, use modules, handle exceptions, debug logic errors, and create classes in Python.

## AI Engineering Relevance

Functions, modules, exceptions, debugging, and OOP help make larger AI programs easier to organize, test, reuse, and maintain.

## AI Usage Log

### Tool Used

ChatGPT

### What I Asked

I asked for help understanding the Lab 03 tasks and organizing the Python files and code.

### What I Used

I used explanations and coding guidance for functions, modules, exceptions, debugging, and OOP.

### What I Verified or Changed Myself

I ran the programs, checked the outputs, tested different inputs, and verified the code myself.
