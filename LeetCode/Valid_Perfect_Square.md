
# Valid Perfect Square

Date: 19-08-2024

## Solution
#### Python
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        num = num ** 0.5
        if int(num) == num:
            return True
        else:
            return False
```
        