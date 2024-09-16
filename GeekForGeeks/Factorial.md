
# Factorial

Date: 16-09-2024

## Solution
#### Python
```python
class Solution:
    def factorial (self, N):
        fact = 1
        for i in range(1, N+1):
            fact *= i
        return fact
```
        