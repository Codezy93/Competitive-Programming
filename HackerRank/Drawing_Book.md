# Drawing Book

Date: 2024-10-18 00:00:00

## Solution

#### Python
```python
def pageCount(n, p):
    f = p // 2
    b = (n - p) / 2
    return min(f, math.ceil(b) if n % 2 == 0 else math.floor(b))
 ```