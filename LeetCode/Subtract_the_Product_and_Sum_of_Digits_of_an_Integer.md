
# Subtract the Product and Sum of Digits of an Integer

Date: 06-09-2024

## Solution
#### Python
```python
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1
        for i in str(n):
            sum += int(i)
            prod *= int(i)
        return prod-sum
```
        