# Substrings of Size Three with Distinct Characters

Date: 2024-10-31 00:00:00

## Solution

#### Python
```python
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)-2):
            if len(set(list(s[i:i+3]))) == 3:
                count += 1
        return count
 ```