# Puzzles

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
n, m = map(int, input().split())
p = list(map(int, input().split()))
s = 1000
p.sort()
if m == n:
    s = p[m - 1] - p[0]
else:
    for j in range(m - n + 1):
        d = 0
        for k in range(n - 1):
            d += p[j + k + 1] - p[j + k]
        if d < s:
            s = d
print(s)
 ```