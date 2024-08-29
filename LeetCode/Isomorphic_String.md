
# Isomorphic String

Date: 29-08-2024

## Solution
#### Python
```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        l1 = {}
        curr_l1 = 0
        l2 = {}
        curr_l2 = 0
        for x, i in enumerate(s):
            if i not in l1:
                l1[i] = curr_l1
                s[x] = l1[i]
                curr_l1 += 1
            else:
                s[x] = l1[i]
        for x, i in enumerate(t):
            if i not in l2:
                l2[i] = curr_l2
                t[x] = l2[i]
                curr_l2 += 1
            else:
                t[x] = l2[i]
        if s == t:
            return True
        else:
            return False
```
        