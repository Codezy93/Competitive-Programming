
# Third Maximum Number

Date: 25-08-2024

## Solution
#### Python
```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)>=3:
            return nums[-3]
        else:
            return nums[-1]
```
        