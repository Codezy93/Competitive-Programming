# Service Lane

Date: 2024-10-07 21:37:19.085381

## Solution

#### Python
```python
def serviceLane(n, cases, width):
    return [min(width[i[0]:i[1]+1]) for i in cases]
 ```