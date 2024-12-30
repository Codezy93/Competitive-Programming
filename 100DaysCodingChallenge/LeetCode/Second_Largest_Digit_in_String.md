# Second Largest Digit in String

Date: 2024-10-23 00:00:00

## Solution

#### Python
```python
class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set([int(x) if x in "1234567890" else None for x in s])
        if None in digits:
            digits.remove(None)
        if len(digits) <= 1:
            return -1
        else:
            temp = max(digits)
            digits.remove(temp)
            return max(digits)
 ```