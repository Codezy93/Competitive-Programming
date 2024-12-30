
# Reverse a string using stack

Date: 05-09-2024

## Solution
#### Python
```python
def reverse(S):
    stack = []
    for i in S:
        stack.insert(0, i)
    S = ""
    for i in stack:
        S += i
    return S
```
        