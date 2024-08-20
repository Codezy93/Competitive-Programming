
# Squares of a sorted array

Date: 20-08-2024

## Solution
#### Python
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [x**2 for x in nums]
        nums.sort()
        return nums
```
        