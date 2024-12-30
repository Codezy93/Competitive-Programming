
# Second Largest

Date: 08-08-2024

## Solution
#### Python
```python
class Solution:
    def print2largest(self, arr):
        arr = sorted(set(arr))
        if len(arr) == 1:
            return -1
        else:
            return arr[-2]
```