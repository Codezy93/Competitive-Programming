# Operation to Zero

Date: 2024-10-11 00:00:00

## Solution

#### Python
```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while True:
            if num1==0 or num2==0:
                break
            elif num1 > num2:
                num1 -= num2
            elif num1 < num2:
                num2 -= num1
            else:
                num1-=num2
            count += 1
        return count
 ```