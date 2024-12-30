# Required Remainder

Date: 2024-11-06 00:00:00

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    if (n % x) - y >= 0:
        k = n - ((n % x) - y)
    else:
        k = n - (x + ((n % x) - y))
    print(k)
 ```