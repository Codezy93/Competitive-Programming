# Array Duplicates

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
class Solution:
    def findDuplicates(self, arr):
        map = {}
        for i in arr:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        for i in map:
            if map[i] > 1:
                res.append(i)
        res.sort()
        return res
 ```