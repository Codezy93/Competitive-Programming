
# Common in 3 sorted array

Date: 11-08-2024

## Solution
#### Python
```python
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr3 = set(arr3)
        return sorted(arr1 & arr2 & arr3)
```
        