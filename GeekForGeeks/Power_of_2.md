
# Power of 2

Date: 09-08-2024

## Solution
#### Python
```python
class Solution:
    def isPowerofTwo(self,n : int ) -> bool:
        if n <= 0:
            return False
        else:
            return n & (n - 1) == 0
```
        