
# Perimeter of squares in a rectangle

Date: 11-08-2024

## Solution
#### Python
```python
def perimeter(n):
    series = [1, 1]
    for _ in range(n-1):
        series.append(series[-1] + series[-2])
    return sum(series)*4
```
        