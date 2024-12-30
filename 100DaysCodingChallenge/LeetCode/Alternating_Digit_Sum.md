# Alternating Digit Sum

Date: 2024-11-05 00:00:00

## Solution

#### Python
```python
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sum = 0
        n = str(n)
        sign = True
        for i in n:
            if sign:
                sum += int(i)
            else:
                sum += (-1*int(i))
            sign = not sign
        return sum
 ```