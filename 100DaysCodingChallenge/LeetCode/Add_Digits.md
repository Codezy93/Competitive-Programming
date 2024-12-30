
# Add Digits

Date: 11-08-2024

## Solution
#### Python
```python
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = [int(x) for x in list(str(num))]
            num = sum(num)
        return num
```
        