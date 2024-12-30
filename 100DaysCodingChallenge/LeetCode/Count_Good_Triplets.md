# Count Good Triplets

Date: 2024-10-06 19:39:58.074223

## Solution

#### Python
```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        out = 0
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j+1, len(arr)):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        out += 1
        return out
 ```