
# Implement StrStr

Date: 26-09-2024

## Solution
#### Python
```python
def strstr(s,x):
    if x not in s:
        return -1
    else:
        for i in range(0, len(s)-len(x)+1):
            if s[i:i+len(x)] == x:
                return i
```
        