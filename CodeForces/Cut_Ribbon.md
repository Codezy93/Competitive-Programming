# Cut Ribbon

Date: 2024-10-29 00:00:00

## Solution

#### Python
```python
n, a, b, c = map(int, input().split())
r = [0] * 5001
r[0] = 1
for i in range(1, n + 1):
    if i - a >= 0 and r[i - a] > 0:
        r[i] = max(r[i], r[i - a] + 1)
    if i - b >= 0 and r[i - b] > 0:
        r[i] = max(r[i], r[i - b] + 1)
    if i - c >= 0 and r[i - c] > 0:
        r[i] = max(r[i], r[i - c] + 1)
print(r[n] - 1)
 ```