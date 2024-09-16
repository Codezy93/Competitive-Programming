
# Find the unique number

Date: 16-09-2024

## Solution
#### Python
```python
def find_uniq(arr):
    s = set(arr)
    for x in s:
        if arr.count(x) == 1:
            return x
```
        