
# Rotate Array

Date: 22-08-2024

## Solution
#### Python
```python
class Solution:
    def rotateArr(self,A,D,N):
        D = D%N
        A[:] = A[D:N] + A[0:D]
        return A
```
        