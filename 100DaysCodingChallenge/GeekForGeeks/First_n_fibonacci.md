
# First n fibonacci

Date: 04-09-2024

## Solution
#### Python
```python
class Solution:
    def printFibb(self,n):
        if n == 1:
            return ["1"]
        fib = ["1","1"]
        while len(fib) < n:
            fib.append(str(int(fib[-1]) + int(fib[-2])))
        return  fib
```
        