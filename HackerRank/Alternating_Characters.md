
# Alternating Characters

Date: 28-09-2024

## Solution
#### Python
```python
def alternatingCharacters(s):
    deletions = 0
    s = list(s)
    index = 0
    while index < len(s)-1:
        if s[index] == s[index+1]:
            del s[index+1]
            deletions += 1
        else:
            index += 1
    return deletions
```
        