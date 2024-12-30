# If you cant sleep just count sheep

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
def count_sheep(n):
    out = []
    for i in range(1, n+1):
        out.append(f"{i} sheep...")
    return "".join(out)
 ```