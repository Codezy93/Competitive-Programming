
# Kth Smallest

Date: 09-09-2024

## Solution
#### Python
```python
class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    def quick_select(self, arr, low, high, k):
        if low <= high:
            pi = self.partition(arr, low, high)
            if pi == k:
                return arr[pi]
            elif pi > k:
                return self.quick_select(arr, low, pi - 1, k)
            else:
                return self.quick_select(arr, pi + 1, high, k)
    def kthSmallest(self, arr, k):
        return self.quick_select(arr, 0, len(arr) - 1, k - 1)
```
        