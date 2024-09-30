
# Uncommon Characters

Date: 30-09-2024

## Solution
#### Python
```python
class Solution:
    def UncommonChars(self,A, B):
        A = list(A)
        B = list(B)
        a = set(A).difference(set(B))
        b = set(B).difference(set(A))
        return "".join(sorted(a.union(b))) if len(a)+len(b)>0 else -1
```
        