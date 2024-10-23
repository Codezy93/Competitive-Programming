# Non Repeating Characters

Date: 2024-10-23 00:00:00

## Solution

#### Python
```python
class Solution:
    def nonRepeatingChar(self,s):
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in map:
            if map[i] == 1:
                return i
        else:
            return -1
 ```