
# Base 7

Date: 17-08-2024

## Solution
#### Python
```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        bits = []
        while num != 0:
            bits.append(str(num % 7))
            num //= 7
        result = ''.join(reversed(bits))
        return f"-{result}" if negative else result
```
        