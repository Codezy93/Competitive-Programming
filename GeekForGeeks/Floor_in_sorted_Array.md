
# Floor in sorted Array

Date: 23-08-2024

## Solution
#### Python
```python
class Solution:
    def findFloor(self,A,N,X):
        index = 0
        change = False
        for h, i in enumerate(A):
            if i <= X and i >= A[index]:
                index = h
                change = True
        return index if change else -1
```
        