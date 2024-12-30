# Check the exam

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
def check_exam(arr1,arr2):
    n = sum([0 if y == "" else (4 if x == y else -1) for x, y in zip(arr1, arr2)])
    return n if n > 0 else 0
 ```