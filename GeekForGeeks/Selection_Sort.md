
# Selection Sort

Date: 27-08-2024

## Solution
#### Python
```python
class Solution: 
    def selectionSort(self, arr,n):
            for curr in range(len(arr)):
                min_index = curr
                for i in range(curr + 1, len(arr)):
                    if arr[i] < arr[min_index]:
                        min_index = i
                if min_index != curr:
                    arr[curr], arr[min_index] = arr[min_index], arr[curr]
            arr = [str(x) for x in arr]
            return(" ".join(arr))
```
        