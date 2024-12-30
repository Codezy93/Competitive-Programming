
# Prime Number

Date: 25-08-2024

## Solution
#### Python
```python
class Solution:
    def isPrime (self, N):
        if N <= 1:
            return 0
        for i in range(2, int(N**0.5)+1):
            if N%i==0:
                return 0
        else:
            return 1
```
        