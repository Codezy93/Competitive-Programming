# Yet Another Integer Problem

Date: 2024-11-01 00:00:00

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    a, b = map(int, input().split(" "))
    x = abs(a - b)
    steps = x // 10 if x % 10 == 0 else (x // 10 + 1)
    print(steps)
 ```