# Remove Duplicates from Sorted Array

Date: 07-08-2024

## Solution
#### Python
```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = sorted(set(nums))
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]
        return len(unique_nums)
```