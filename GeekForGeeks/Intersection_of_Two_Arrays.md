
# Intersection of Two Arrays

Date: 10-09-2024

## Solution
#### Python
```python
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        return len(set(a).intersection(set(b)))
```
        