# Sum of elements in a matrix

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
class Solution:
    def sumOfMatrix(self,N,M,Grid):
        s = 0
        for i in Grid:
            s = s + sum(i)
        return s
 ```