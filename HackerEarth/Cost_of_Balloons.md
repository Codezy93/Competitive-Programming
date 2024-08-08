
# Cost of Balloons

Date: 08-08-2024

## Solution
#### Python
```python
iter = int(input())
for _ in range(0, iter):
    x, y = map(int, input().split())
    total = 0
    p = 0
    q = 0
    for i in range(0, int(input())):
        a, b = map(int, input().split())
        p = p + a
        q = q + b
    if(p >= q):
        if(x > y):
            total = total + (p*y) + (q*x)
        else:
            total = total + (p*x) + (q*y)
    else:
        if(x > y):
            total = total + (q*y) + (p*x)
        else:
            total = total + (q*x) + (p*y)
    print(total)
```