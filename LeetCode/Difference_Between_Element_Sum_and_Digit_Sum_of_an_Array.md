
# Difference Between Element Sum and Digit Sum of an Array

Date: 02-09-2024

## Solution
#### Python
```python
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elem_sum = 0
        digit_sum = 0
        for i in nums:
            elem_sum += i
            for j in str(i):
                digit_sum += int(j)
        return abs(elem_sum-digit_sum)
```
        