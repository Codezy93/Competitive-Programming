
# Power of Four

Date: 30-09-2024

## Solution
#### Python
```python
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0:
            a = math.log(n, 4)
            return a-int(a) == 0
        else:
            return False
```
        