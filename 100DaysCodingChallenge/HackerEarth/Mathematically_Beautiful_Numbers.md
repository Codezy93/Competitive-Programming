# Mathematically Beautiful Numbers

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
def is_mathematically_beautiful(N, K):
    if K == 1:
        return N == 1
    while N > 0:
        d = N % K
        if d > 1:
            return False
        N = N // K
    return True
T = int(input())
for _ in range(T):
    N_str, K_str = input().split()
    N = int(N_str)
    K = int(K_str)
    if is_mathematically_beautiful(N, K):
        print("YES")
    else:
        print("NO")
 ```