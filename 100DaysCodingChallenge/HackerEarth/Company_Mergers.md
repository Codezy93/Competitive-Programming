# Company Mergers

Date: 2024-10-13 19:26:26.421996

## Solution

#### Python
```python
from collections import Counter
from operator import itemgetter
n = int(input())
m = int(input())
data = []
flat = []
count = 0
for _ in range(n):
    ids = list(map(int, input().strip().split()))
    if ids in data:
        count += 1
    else:
        data.append(ids)
        flat.extend(ids)
counter = Counter(flat)
_, max_c = max(counter.items(), key=itemgetter(1))
if max_c > 2:
    _, min_c = min(counter.items(), key=itemgetter(1))
    count += max_c - max(2, min_c) + 1
if (count > n - 2 and count > 0) or (len(data) == 1 and n > 1):
    count = n - 2
print(count)
 ```