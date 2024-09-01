
# Abbrevate a Two Word Name

Date: 01-09-2024

## Solution
#### Python
```python
def abbrev_name(name):
    return ".".join([i[0] for i in name.upper().split(" ")])
```
        