
# Isograms

Date: 23-08-2024

## Solution
#### Python
```python
def is_isogram(string):
    return len(set(string.lower())) == len(string.lower())
```
        