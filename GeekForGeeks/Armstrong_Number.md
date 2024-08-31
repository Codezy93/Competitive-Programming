
# Armstrong Number

Date: 31-08-2024

## Solution
#### Python
```python
class Solution:
    def armstrongNumber (self, n):
        sum = 0
        for i in str(n):
            sum += int(i)**3
        return "true" if sum == n else "false"
```
        