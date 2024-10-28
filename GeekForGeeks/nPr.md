# nPr

Date: 2024-10-28 00:00:00

## Solution

#### Python
```python
class Solution:
    def nPr(self, n, r):
        N = self.fact(n)
        D = self.fact(n-r)
        return (int(N/D))
    def fact(self, n):
        f = 1
        for i in range(1, n+1):
            f = f * i
        return f
 ```