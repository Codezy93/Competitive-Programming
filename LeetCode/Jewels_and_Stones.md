
# Jewels and Stones

Date: 18-08-2024

## Solution
#### Python
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        for i in jewels:
            num += stones.count(i)
        return num
```
        