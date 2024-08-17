
# Triangle shrinking downwards

Date: 17-08-2024

## Solution
#### Python
```python
class Solution:
    def triDownwards(self, S):
        out = []
        count = 0
        for i in range(len(S)):
            out.append("."*count + S[count:len(S)])
            count += 1
        return "".join(out)
```
        