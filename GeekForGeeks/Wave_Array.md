# Wave Array

Date: 2024-10-09 17:57:48.744318

## Solution

#### Python
```python
class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        arr.sort()
        if n%2==0:
            for i in range(0, n-1, 2):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        else:
            for i in range(0, n-2, 2):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
 ```