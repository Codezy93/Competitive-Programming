
# Monk being Monitor

Date: 29-08-2024

## Solution
#### Python
```python
from collections import Counter
T = int(input())
for i in range(T):
    l = []
    N = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    c = list(c.values())
    c.sort()
    if (c[-1] - c[0] > 0):
        print(c[-1] - c[0])
    else:
        print(-1)
```
        