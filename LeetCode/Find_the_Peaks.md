
# Find the Peaks

Date: 31-08-2024

## Solution
#### Python
```python
class Solution:
    def findPeaks(self, arr: List[int]) -> List[int]:
        index = []
        for x in range(1, len(arr)-1):
            if arr[x] > arr[x-1] and arr[x] > arr[x+1]:
                index.append(x)
        return index
```
        