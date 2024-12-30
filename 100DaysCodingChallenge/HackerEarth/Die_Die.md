# Die Die

Date: 2024-10-27 00:00:00

## Solution

#### Python
```python
for _ in range(0, int(input())):
    N = int(input())
    P = 2
    mod = 10**9 + 7
    Q = pow(2, N, mod)
    Q_inv = pow(Q, mod - 2, mod)
    print((P * Q_inv) % mod)
 ```