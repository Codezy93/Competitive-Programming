
# Determining Number

Date: 28-09-2024

## Solution
#### Python
```python
from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
a = Counter(arr)
ans = []
for k,v in a.items():
    if v==1:
        ans.append(k)
ans.sort()
print(*ans)
```
        