# Find Kth Rotation

Date: 2024-10-13 19:26:26.421996

## Solution

#### Python
```python
class Solution:
    def findKRotation(self, arr):
        max_val = arr.index(max(arr))+1
        if max_val == len(arr):
            return 0
        else:
            return max_val
 ```