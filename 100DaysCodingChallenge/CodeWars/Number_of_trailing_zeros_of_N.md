
# Number of trailing zeros of N

Date: 13-08-2024

## Solution
#### Python
```python
def zeros(n):
    if n <= 0:
        return 0
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    return count
```
        