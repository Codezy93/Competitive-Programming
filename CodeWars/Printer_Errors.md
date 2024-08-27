
# Printer Errors

Date: 27-08-2024

## Solution
#### Python
```python
def printer_error(s):
    not_allowed = "nopqrstuvwxyz"
    times = 0
    for i in s:
        if i in not_allowed:
            times += 1
    return f"{times}/{len(s)}"
```
        