
# Shortest Word

Date: 11-09-2024

## Solution
#### Python
```python
def find_short(s):
    return min([len(i) for i in s.split(' ')])
```
        