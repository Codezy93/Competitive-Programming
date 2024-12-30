# Maximum 69 Number

Date: 2024-10-03 00:00:00

## Solution

#### Python
```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i, j in enumerate(num):
            if j=="6":
                num[i]="9"
                break
        return int("".join(num))
 ```