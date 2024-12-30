# Pattern 6

Date: 2024-10-20 00:00:00

## Solution

#### Python
```python
class Solution:
    def printTriangle(self, N):
        for i in range(N, 0, -1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
 ```