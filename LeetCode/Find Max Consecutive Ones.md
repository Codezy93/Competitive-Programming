
# Find Max Consecutive Ones

Date: 23-08-2024

## Solution
#### Python
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max([len(x) for x in "".join([str(i) for i in nums]).split("0")])
```