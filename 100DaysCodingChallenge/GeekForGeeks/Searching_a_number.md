
# Searching a number

Date: 24-09-2024

## Solution
#### Python
```python
class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        for i, j in enumerate(arr):
            if j==k:
                return i+1
        else:
            return -1
```
        