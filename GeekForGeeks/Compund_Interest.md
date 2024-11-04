# Compund Interest

Date: 2024-11-04 00:00:00

## Solution

#### Python
```python
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        R = 1 + (R/(100*N))
        a = P * (R**(N*T))
        return int(a)
 ```