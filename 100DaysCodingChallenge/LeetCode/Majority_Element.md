
# Majority Element

Date: 10-08-2024

## Solution
#### Python
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = list(set(nums))
        for i in unique:
            if nums.count(i) > len(nums)/2:
                return i
```
        