
# Split String

Date: 26-08-2024

## Solution
#### Python
```python
def solution(s):
    out = []
    if len(s) % 2 != 0:
        s = s + "_"
    for i in range(0, len(s)-1, 2):
        out.append(s[i:i+2])
    return out
```
        