# Selection of Cities

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
MOD = 1000000007
def powg(a, b):
    ans = 1
    while b > 0:
        if b & 1:
            ans = (ans * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return ans % MOD
for _ in range(int(input())):
    out = 1
    print((powg(2, int(input())) - 1) % MOD)
 ```