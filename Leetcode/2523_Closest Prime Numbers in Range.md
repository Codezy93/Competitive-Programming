# 2523. Closest Prime Numbers in Range

---

Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

  * `left <= num1 < num2 <= right `.
  * `num1` and `num2` are both **prime ** numbers.
  * `num2 - num1` is the **minimum ** amongst all other pairs satisfying the above conditions.



Return _the positive integer array_ `ans = [num1, num2]`. _If there are multiple pairs satisfying these conditions, return the one with the minimum_ `num1` _value or_ `[-1, -1]` _if such numbers do not exist._

A number greater than `1` is called **prime ** if it is only divisible by `1` and itself.

 

**Example 1:**


**Input:** left = 10, right = 19
**Output:** [11,13]
**Explanation:** The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.


**Example 2:**


**Input:** left = 4, right = 6
**Output:** [-1,-1]
**Explanation:** There exists only one prime number in the given range, so the conditions cannot be satisfied.


 

**Constraints:**

  * `1 <= left <= right <= 106`

---

## Solution



---

## Code
```python
class Solution:
  def closestPrimes(self, left: int, right: int) -> list[int]:
    isPrime = self._sieveEratosthenes(right + 1)
    primes = [i for i in range(left, right + 1) if isPrime[i]]

    if len(primes) < 2:
      return [-1, -1]

    minDiff = math.inf
    num1 = -1
    num2 = -1

    for a, b in zip(primes, primes[1:]):
      diff = b - a
      if diff < minDiff:
        minDiff = diff
        num1 = a
        num2 = b

    return [num1, num2]

  def _sieveEratosthenes(self, n: int) -> list[bool]:
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n**0.5) + 1):
      if isPrime[i]:
        for j in range(i * i, n, i):
          isPrime[j] = False
    return isPrime
```