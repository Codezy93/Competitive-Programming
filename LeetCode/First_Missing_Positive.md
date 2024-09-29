
# First Missing Positive

Date: 29-09-2024

## Solution
#### Python
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if 1 in nums:
            index = nums.index(1) 
        else:
            return 1
        for i in range(index, len(nums)-1):
            if nums[i+1]-nums[i] != 1:
                return nums[i]+1
        else:
            return nums[-1]+1
```
        