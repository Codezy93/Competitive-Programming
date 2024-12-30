
# Missing Numbers

Date: 29-09-2024

## Solution
#### Python
```python
class Solution:
    def missingNumber(self, n, arr):
        arr.sort()
        for i, j in enumerate(arr):
            if i+1 != j:
                return i+1
        else:
            return n
```
        