
# Equilibrium Point

Date: 07-09-2024

## Solution
#### Python
```python
class Solution:
    def equilibriumPoint(self, arr):
        n = len(arr)
        if n == 1:
            return 1
        total_sum = sum(arr)
        left_sum = 0
        for i in range(n):
            total_sum -= arr[i]
            if left_sum == total_sum:
                return i + 1
            left_sum += arr[i]
        return -1
```
        