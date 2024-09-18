
# Rotating Array

Date: 18-09-2024

## Solution
#### Python
```python
class Solution:
    def leftRotate(self, arr, d):
        temp = arr[0:d]
        del arr[0:d]
        arr[:] = arr + temp
```
        