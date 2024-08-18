
# Union of Two Sorted Arrays

Date: 18-08-2024

## Solution
#### Python
```python
class Solution:
    def findUnion(self,arr1,arr2,n,m):
        return sorted(set(arr1).union(set(arr2)))
```
        