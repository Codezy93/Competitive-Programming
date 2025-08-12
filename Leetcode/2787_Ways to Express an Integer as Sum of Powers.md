# 2787. Ways to Express an Integer as Sum of Powers

---

Given two **positive ** integers `n` and `x`.

Return _the number of ways_`n` _can be expressed as the sum of the_`xth` _power of **unique ** positive integers, in other words, the number of sets of unique integers _`[n1, n2, ..., nk]`_where_`n = n1x + n2x + ... + nkx` _._

Since the result can be very large, return it modulo `109 + 7`.

For example, if `n = 160` and `x = 3`, one way to express `n` is `n = 23 + 33 + 53`.

 

**Example 1:**


**Input:** n = 10, x = 2
**Output:** 1
**Explanation:** We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.


**Example 2:**


**Input:** n = 4, x = 1
**Output:** 2
**Explanation:** We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.


 

**Constraints:**

  * `1 <= n <= 300`
  * `1 <= x <= 5`

---

## Solution



---

## Code
```python
class Solution:
  def numberOfWays(self, n: int, x: int) -> int:
    MOD = 1_000_000_007
    dp = [1] + [0] * n
    for a in range(1, n + 1):
      ax = a**x
      if ax > n:
        break
      for i in range(n, ax - 1, -1):
        dp[i] += dp[i - ax]
        dp[i] %= MOD
    return dp[n]
```
