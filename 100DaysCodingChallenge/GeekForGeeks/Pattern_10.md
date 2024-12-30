# Pattern 10

Date: 2024-10-22 00:00:00

## Solution

#### Python
```python
class Solution:
    def printTriangle(self, n):
        for i in range(1, n):
            print("* "*i)
        for i in range(n, 0, -1):
            print("* "*i)
 ```