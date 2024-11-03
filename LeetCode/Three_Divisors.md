# Three Divisors

Date: 2024-11-03 00:00:00

## Solution

#### Python
```python
class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False
        count = 0
        for i in range(1, n+1):
            if n%i == 0:
                count += 1
        return count == 3
 ```