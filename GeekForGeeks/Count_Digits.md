
# Count Digits

Date: 20-08-2024

## Solution
#### Python
```python
class Solution:
    def evenlyDivides (self, N):
        N = str(N)
        digits = [int(x) for x in N]
        N = int(N)
        divs = 0
        for i in digits:
            if i != 0 and N%i == 0:
                divs += 1
        return divs
```
        