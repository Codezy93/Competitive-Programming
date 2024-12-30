# Find triplets with zero sum

Date: 2024-11-12 22:19:35.073070

## Solution

#### Python
```python
class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if arr[i]+arr[j]+arr[k] == 0:
                        return True
        else:
            return False
 ```