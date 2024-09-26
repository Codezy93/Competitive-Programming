
# Reverse Integer

Date: 26-09-2024

## Solution
#### Python
```python
class Solution:
    def check(self, x):
        if x<-2147483648 or x>2147483647:
            return 0
        else:
            return x
    def reverse(self, x: int) -> int:
        if self.check(x) == 0:
            return 0
        if x < 0:
            num = int("-" + str(abs(x))[::-1])
            return self.check(num)
        else:
            num = int(str(x)[::-1])
            return self.check(num)
```
        