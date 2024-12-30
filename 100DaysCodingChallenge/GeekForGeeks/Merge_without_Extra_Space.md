
# Merge without Extra Space

Date: 02-10-2024

## Solution
#### Python
```python
class Solution:
    def merge(self,arr1,arr2,n,m):
        arr1[:] = sorted(arr1+arr2)
        arr2[:] = arr1[n:n+m]
        arr1[:] = arr1[0:n]
```
        