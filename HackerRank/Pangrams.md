# Pangrams

Date: 2024-10-24 00:00:00

## Solution

#### Python
```python
def pangrams(s):
    s = s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return 'not pangram'
    else:
        return 'pangram'
 ```