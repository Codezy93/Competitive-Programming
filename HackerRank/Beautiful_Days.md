# Beautiful Days

Date: 2024-10-09 17:57:48.744318

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