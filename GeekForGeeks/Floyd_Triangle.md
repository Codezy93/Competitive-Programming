# Floyd Triangle

Date: 2024-10-27 00:00:00

## Solution

#### Python
```python
class Solution:
    def printFloydTriangle(self, N):
        count = 1
        i = 1
        for x in range(0 ,N):
            for j in range(0, i):
                print(count, end=" ")
                count += 1
            print()
            i += 1
 ```