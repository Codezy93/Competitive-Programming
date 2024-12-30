
# Replace Question Marks

Date: 13-09-2024

## Solution
#### Python
```python
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        if len(s) == 1:
            if s[0] == "?":
                return 'a'
            else:
                return s[0]
        for i, j in enumerate(s):
            if j == "?":
                if i == 0:
                    if s[i+1] != 'a':
                        s[i] = 'a'
                    else:
                        s[i] = 'b'
                elif i == len(s)-1:
                    if s[i-1] != 'a':
                        s[i] = 'a'
                    else:
                        s[i] = 'b'
                else:
                    if s[i+1] != 'a' and s[i-1] != 'a':
                        s[i] = 'a'
                    elif s[i+1] != 'b' and s[i-1] != 'b':
                        s[i] = 'b'
                    else:
                        s[i] = 'c'
        return ''.join(s)
```
        