
# Counting Bits

Date: 22-08-2024

## Solution
#### Python
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        start = "0000"
        increment = "0001"
        for i in range(0, n):
            start = bin(int(start, 2) + int(increment, 2))
            bits.append(start.count("1"))
        return bits
```
        