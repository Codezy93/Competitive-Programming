# Print 1 to n without using loops

Date: 2024-11-03 00:00:00

## Solution

#### Python
```python
class Solution:
    def printTillN(self, N):
        if N == 0:
            return 1
        else:
            self.printTillN(N-1)
            print(N, end = " ")
 ```