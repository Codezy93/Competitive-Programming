
# Remove Duplicates from sorted array

Date: 28-08-2024

## Solution
#### Python
```python
class Solution:
    def remove_duplicate(self, arr):
        if not arr:
            return 0
        unique_index = 0
        for i in range(1, len(arr)):
            if arr[i] != arr[unique_index]:
                unique_index += 1
                arr[unique_index] = arr[i]
        return unique_index + 1
```
        