# Reverse Digits

Date: 2024-11-02 00:00:00

## Solution

#### Python
```python
class Solution:
    def reverse_digit(self, n):
        n = list(str(n))
        n.reverse()
        while n[0] == '0':
            del n[0]
        out = ""
        for i in n:
            out = out + i
        return out
 ```