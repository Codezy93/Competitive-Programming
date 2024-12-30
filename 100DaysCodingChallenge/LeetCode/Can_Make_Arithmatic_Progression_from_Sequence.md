
# Can Make Arithmatic Progression from Sequence

Date: 27-09-2024

## Solution
#### Python
```python
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        cd = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if arr[i]-arr[i-1] != cd:
                return False
        else:
            return True
```
        