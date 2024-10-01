
# Categorize Members

Date: 01-10-2024

## Solution
#### Python
```python
def open_or_senior(data):
    for i, j in enumerate(data):
        data[i] = 'Senior' if j[0] >= 55 and j[1] > 7 else 'Open'
    return data
```
        