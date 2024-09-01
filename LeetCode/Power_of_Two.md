
# Power of Two

Date: 01-09-2024

## Solution
#### Python
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 0): 
            return False
        while (n != 1): 
                if (n % 2 != 0): 
                    return False
                n = n // 2
        return True
```
        