# Playing with digits

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i)**p
        p += 1
    if sum%n == 0:
        return sum//n
    return -1
 ```