
# Number of 1 Bits

Date: 09-08-2024

## Solution
#### Python
```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n).replace('0b', '')
        n = n.replace('0', "")
        return len(n)
```
        