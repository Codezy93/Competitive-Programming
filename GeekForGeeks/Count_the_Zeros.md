
# Count the Zeros

Date: 02-09-2024

## Solution
#### Python
```python
class Solution:
    def countZeroes(self, arr):
        arr = [x^1 for x in arr]
        return sum(arr)
```
        