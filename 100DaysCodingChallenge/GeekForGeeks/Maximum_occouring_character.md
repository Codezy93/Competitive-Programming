
# Maximum occouring character

Date: 28-09-2024

## Solution
#### Python
```python
class Solution:
    def getMaxOccurringChar(self,s):
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        max_, maxl = 0, ""
        for i in map:
            if map[i] == max_ and i < maxl:
                max_ = map[i]
                maxl = i
            elif map[i] > max_:
                max_ = map[i]
                maxl = i
            else:
                pass
        return maxl
```
        