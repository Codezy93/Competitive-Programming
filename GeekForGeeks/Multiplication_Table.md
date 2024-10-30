# Multiplication Table

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
class Solution:
    def getTable(self,N):
        a = []
        for i in range(1, 11):
            a.append(N*i)
        return a
 ```