# Break CamelCase

Date: 2024-10-06 19:39:58.074223

## Solution

#### Python
```python
def solution(s):
    out = []
    for i in s:
        if i.isupper():
            out.append(" ")
            out.append(i)
        else:
            out.append(i)
    return "".join(out)
 ```