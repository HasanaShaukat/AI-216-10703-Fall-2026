# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced
- Lists
- Tuples
- Dictionaries
- Sets
- Comprehensions
- `enumerate()`
- `zip()`
- Sorting and counting records
- Data structure selection
- Clean code
- File organization

## Tasks Completed
1. Lists
2. Aliasing vs Copying
3. Tuples
4. Dictionaries
5. Sets
6. Comprehensions
7. `enumerate()` and `zip()`
8. Data Structure Selection
9. Prediction Analysis — Part A and Part B

## Data Structure Decisions
- Lists are used for ordered collections.
- Tuples are used for fixed values such as image size and required fields.
- Dictionaries are used for structured records and metadata.
- Sets are used for unique labels and set operations.

## Aliasing vs Copying
Assignment between two list variables creates an alias to the same list. `.copy()` creates a separate outer list, but nested dictionaries are still shared. `copy.deepcopy()` creates independent nested objects.

## Hashability
A tuple can be used as a dictionary key because it is immutable and hashable when its elements are hashable. A list cannot be a dictionary key because lists are mutable and unhashable.

## Sets vs Lists for Validation
Sets make validation clearer because union, intersection, and difference directly express the required operations. Set membership checks are also efficient because sets use hash-based lookup.

## Clean-Code Refactoring
The original Task 9 code used unclear variable names such as `x`, `y`, `z`, and `d`, and mixed processing responsibilities together. The refactored version uses descriptive names, named constants, and separate functions/files for preprocessing and analysis.

## Handling Incomplete Records
Records missing required fields are skipped from analysis but their IDs are reported. Labels are normalized by stripping spaces and converting them to lowercase. Normalization creates new records so the raw input remains unchanged.

## Edge Cases Tested
- Empty collections
- Duplicate values
- Confidence exactly equal to 0.80
- Missing confidence field
- Unexpected labels
- Label normalization without changing raw records

## What I Found Difficult
Understanding the difference between aliasing, shallow copying, and deep copying was the most difficult part.

## What I Learned
I learned how to select Python data structures based on the meaning of the data and how to organize data-processing code into smaller responsibilities.

## AI Engineering Relevance
Data structures and clean code are important for preprocessing, configuration, model outputs, validation, and maintainability.

## AI Usage Log

### Tool Used
ChatGPT

### What I Asked
Help with understanding and implementing the Week 4 Python data-structure and clean-code tasks.

### What I Used
Explanations and implementation guidance for the required tasks.

### What I Verified or Changed Myself
I should run and verify the programs, check outputs, and make any required changes before submission.
