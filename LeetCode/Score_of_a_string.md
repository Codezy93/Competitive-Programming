
# Score of a string

Date: 11-09-2024

## Solution
#### Python
```python
class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(0, len(s)-1):
            sum += abs(ord(s[i])-ord(s[i+1]))
        return sum
```
        