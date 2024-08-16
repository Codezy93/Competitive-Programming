
# Peak Element

Date: 16-08-2024

## Solution
#### Python
```python
class Solution:   
    def peakElement(self,arr, n):
        if n==1:
            return 0
        for i in range(1, n):
            if i == n-1:
                if arr[i] >= arr[i-1]:
                    return i
            elif i == 0:
                if arr[i] >= arr[i+1]:
                    return i
            else:
                if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                    return i
        return -1
```
        