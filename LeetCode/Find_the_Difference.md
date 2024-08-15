
# Find the Difference

Date: 15-08-2024

## Solution
#### Python
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in s:
            t.remove(i)
        return t[0]
```
        