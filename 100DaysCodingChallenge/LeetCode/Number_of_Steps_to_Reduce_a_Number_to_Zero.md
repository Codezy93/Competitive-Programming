
# Number of Steps to Reduce a Number to Zero

Date: 10-09-2024

## Solution
#### Python
```python
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
```
        