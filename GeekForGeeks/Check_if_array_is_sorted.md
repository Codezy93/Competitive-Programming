
# Check if array is sorted

Date: 29-08-2024

## Solution
#### Python
```python
class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(0, len(arr)-1):
            if arr[i+1] - arr[i] < 0:
                return False
        else:
            return True
```
        