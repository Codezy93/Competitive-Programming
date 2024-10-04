# Sign of the Product of an Array

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in nums:
            res *= i
        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0
 ```