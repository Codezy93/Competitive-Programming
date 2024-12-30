# Let us understand computers

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
import sys
import bisect
MX = int(1e6)
arr = [0] * (MX + 1)
def prepare_array():
    r = 2
    for i in range(1, MX + 1):
        if i >= r:
            r <<= 1
        arr[i] = (i * r) - 1
prepare_array()
t = int(input())
for _ in range(t):
    x = int(input())
    index = bisect.bisect_left(arr, x, 1, MX + 1)
    print(x - (index - 1))
 ```