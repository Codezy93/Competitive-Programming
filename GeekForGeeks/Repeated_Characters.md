# Repeated Characters

Date: 2024-10-10 18:29:44.688592

## Solution

#### Python
```python
class Solution:
    def firstRep(self, s):
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in map:
            if map[i] > 1:
                return i
        else:
            return -1
 ```