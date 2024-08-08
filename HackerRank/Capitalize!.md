
# Capitalize!

Date: 08-08-2024

## Solution
#### Python
```python
def solve(s):
    s = s.split(" ")
    for i in range(0, len(s)):
        s[i] = s[i].capitalize()
    return " ".join(s)
```