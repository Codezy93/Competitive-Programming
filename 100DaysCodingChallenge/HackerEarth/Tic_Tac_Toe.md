# Tic Tac Toe

Date: 2024-10-29 00:00:00

## Solution

#### Python
```python
MOD = 1000000007
def sum_of_squares(n):
    n = n % MOD
    ans = (n * (n - 1) % MOD * (2 * n - 1) % MOD * 166666668) % MOD
    return ans % MOD
def minimum_rules(n):
    ans = (n % MOD * (n - 1) % MOD * (n - 1) % MOD * 250000002) % MOD
    return ans % MOD
for _ in range(int(input())):
    n = int(input())
    print(minimum_rules(n), sum_of_squares(n))
 ```