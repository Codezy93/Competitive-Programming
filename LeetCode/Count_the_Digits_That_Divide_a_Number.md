# Count the Digits That Divide a Number

Date: 2024-10-05 00:00:00

## Solution

#### Python
```python
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for i in str(num):
            if num%int(i) == 0:
                count += 1
        return count
 ```