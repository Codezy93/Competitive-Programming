
# Compare the triplets

Date: 23-09-2024

## Solution
#### Python
```python
def compareTriplets(a, b):
    c, d = 0, 0
    for i, j in zip(a, b):
        if i > j:
            c += 1
        elif i < j:
            d += 1
        else:
            pass
    return c, d
```
        