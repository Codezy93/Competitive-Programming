
# Add Binary

Date: 08-08-2024

## Solution
#### Python
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = str(bin(int(a,2) + int(b,2)))
        sum = sum.replace("0b", "")
        return sum
```