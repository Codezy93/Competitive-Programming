
# Fibonacci Number

Date: 08-09-2024

## Solution
#### Python
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fib = [1,1]
        while len(fib) < n:
            fib.append(fib[-2]+fib[-1])
        return fib[n-1]
```
        