# Python Subtle Bug: Zero Division Handling

This repository demonstrates a common yet subtle bug in Python related to zero division. The function `function_with_uncommon_error` does not explicitly handle the case where both inputs are zero, leading to unexpected results.

## The Bug

The provided Python code contains a function that performs division of two numbers. However, the code fails to handle the edge case where both inputs are zero, resulting in undefined behavior.

## The Solution

The solution addresses this edge case by adding an explicit check for when both `a` and `b` are zero, returning an appropriate value or raising a specific exception to handle the situation gracefully.  This prevents unexpected errors and improves the robustness of the function.

## How to Run

1. Clone this repository.
2. Run the bug.py file to see the error.
3. Run the bugSolution.py file to see the corrected version.