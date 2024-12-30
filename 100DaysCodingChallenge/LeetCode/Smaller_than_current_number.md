
# Smaller than current number

Date: 23-09-2024

## Solution
#### Python
```python
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0, len(nums)):
            temp = 0
            for j in range(0, len(nums)):
                if nums[j] < nums[i]:
                    temp += 1
            out.append(temp)
        return out
```
        