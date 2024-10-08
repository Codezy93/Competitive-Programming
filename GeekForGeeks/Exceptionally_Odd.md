# Exceptionally Odd

Date: 2024-10-08 09:11:16.441053

## Solution

#### Python
```python
class Solution:
    def getOddOccurrence(self, arr, n):
        map = {}
        for i in arr:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in map:
            if map[i] % 2 != 0:
                return i
 ```