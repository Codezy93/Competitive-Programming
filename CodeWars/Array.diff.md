# Array.diff
Platform: CodeWars

Date: 06/08/2024

## Problem
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

If a value is present in b, all of its occurrences must be removed from the other:

## Input
Two lists a and b.

## Output
Subtracted list

## Solution
```python
def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a
```