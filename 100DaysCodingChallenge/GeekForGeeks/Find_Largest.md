# Find Largest

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
class Solution:
    def findLargest(self, N, S):
        if S == 0 and N > 1:
            return -1
        if S == 0 and N == 1:
            return 0
        num = ""
        for i in range(N):
            if S>=9:
                S-=9
                num = num + '9'
            else:
                num = num + str(S)
                S-=S
        if S == 0:
            return num
        else:
            return -1
 ```