
# Testing 123

Date: 24-09-2024

## Solution
#### Python
```python
def number(lines):
    for i, j in enumerate(lines):
        lines[i] = f"{i+1}: {j}"
    return lines
```
        