
# License Key Formatting

Date: 22-09-2024

## Solution
#### Python
```python
class Solution:
    def ReFormatString(self,s, k):
        s = list(s.replace("-", ""))
        key = []
        while len(s) > 0:
            if len(s) >= k:
                temp = "".join(s[len(s)-k:])
                del s[len(s)-k:]
            elif len(s) < k:
                temp = "".join(s[0:])
                del s[0:]
            temp = temp.upper()
            key.insert(0, temp)
        return "-".join(key)
```
        