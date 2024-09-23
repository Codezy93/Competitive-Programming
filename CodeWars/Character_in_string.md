
# Character in string

Date: 23-09-2024

## Solution
#### Python
```python
def count(s):
    map = {}
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return map
```
        