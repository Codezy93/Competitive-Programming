# Series AP

Date: 2024-11-01 00:00:00

## Solution

#### Python
```python
class Solution:
    def nthTermOfAP(self,A1,A2,n):
        d = A2 - A1
        a = A1
        t = a + ((n-1)*d)
        return t
 ```