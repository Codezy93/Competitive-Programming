
# Binary Search

Date: 26-08-2024

## Solution
#### Python
```python
class Solution:
    def binarysearch(self, arr, k):
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = left+((right-left)//2)
            if arr[mid] == k:
                return mid
            elif k < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            return -1
```
        