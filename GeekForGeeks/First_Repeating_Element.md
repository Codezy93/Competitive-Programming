
# First Repeating Element

Date: 24-08-2024

## Solution
#### Python
```python
class Solution:
    def firstRepeated(self, arr):
        element_count = {}
        for i in range(len(arr)):
            if arr[i] in element_count:
                element_count[arr[i]] += 1
            else:
                element_count[arr[i]] = 1
        for i in range(len(arr)):
            if element_count[arr[i]] > 1:
                return i + 1
        return -1
```
        