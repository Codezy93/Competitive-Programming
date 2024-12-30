
# Array Search

Date: 14-08-2024

## Solution
#### Python
```python
class Solution:
    def search(self,arr, x):
        for i in range(0, len(arr)):
            if arr[i] == x:
                return i
        else:
            return -1
```
        