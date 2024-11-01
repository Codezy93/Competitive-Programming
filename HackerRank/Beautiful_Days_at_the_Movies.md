# Beautiful Days at the Movies

Date: 2024-11-01 00:00:00

## Solution

#### Python
```python
def beautifulDays(i, j, k):
    count = 0
    for x in range(i, j+1):
        if abs(x-int(str(x)[::-1])) % k == 0:
            count += 1
    return count
 ```