
# Divisibility of 8

Date: 13-09-2024

## Solution
#### Python
```python
class Solution:
    def DivisibleByEight(self,s):
        if len(s) <= 3:
            return 1 if int(s)%8 == 0 else -1
        else:
            return 1 if int(s[-3:])%8 == 0 else -1
```
        