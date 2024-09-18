
# Nth Tribonacci Number

Date: 18-09-2024

## Solution
#### Python
```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        trib = [0, 1, 1]
        for i in range(n-2):
            trib.append(sum(trib[-3:]))
        return trib[-1]
```
        