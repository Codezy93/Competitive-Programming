
# Maximum Product

Date: 24-09-2024

## Solution
#### Python
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                temp = (nums[i]-1)*(nums[j]-1)
                if temp > prod:
                    prod = temp
        return prod
```
        