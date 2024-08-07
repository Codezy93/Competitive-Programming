# Array.diff

Date: 06/08/2024

## Solution
#### Python
```python
def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a
```