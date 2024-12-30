# Round up to the next multiple of 5

Date: 2024-10-29 00:00:00

## Solution

#### Python
```python
def round_to_next5(n):
    if n == 0:
        return 0
    if n%5 == 0:
        return n
    return n + (5-(n%5))
 ```