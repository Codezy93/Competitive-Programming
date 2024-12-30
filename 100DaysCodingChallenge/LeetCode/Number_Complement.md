# Number Complement

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num).replace("0b", "").replace("1", "2").replace("0", "1").replace("2", "0"), 2)
 ```