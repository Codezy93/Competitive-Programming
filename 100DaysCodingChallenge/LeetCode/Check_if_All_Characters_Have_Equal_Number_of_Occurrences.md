# Check if All Characters Have Equal Number of Occurrences

Date: 2024-10-24 00:00:00

## Solution

#### Python
```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        map = {}
        for i in s:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        for i in map:
            res.append(map[i])
        return len(set(res)) == 1
 ```