
# Reverse Word in String III

Date: 02-10-2024

## Solution
#### Python
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i, j in enumerate(s):
            s[i] = j[::-1]
        return " ".join(s)
```
        