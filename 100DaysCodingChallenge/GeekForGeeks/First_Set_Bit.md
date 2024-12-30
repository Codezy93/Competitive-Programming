
# First Set Bit

Date: 11-09-2024

## Solution
#### Python
```python
class Solution:
    def getFirstSetBit(self,n):
        if n == 0:
            return 0
        n = list(bin(n).replace("0b", ""))
        n.reverse()
        for i in range(len(n)):
            if n[i] == '1':
                return i+1
```
        