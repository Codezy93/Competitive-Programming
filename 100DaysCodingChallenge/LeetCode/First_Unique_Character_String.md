
# First Unique Character String

Date: 01-10-2024

## Solution
#### Python
```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in map:
            if map[i] == 1:
                return s.index(i)
        else:
            return -1
```
        