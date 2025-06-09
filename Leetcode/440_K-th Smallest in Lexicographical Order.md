# 440. K-th Smallest in Lexicographical Order

---

Given two integers `n` and `k`, return _the_ `kth` _lexicographically smallest integer in the range_ `[1, n]`.

 

**Example 1:**


**Input:** n = 13, k = 2
**Output:** 10
**Explanation:** The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.


**Example 2:**


**Input:** n = 1, k = 1
**Output:** 1


 

**Constraints:**

  * `1 <= k <= n <= 109`

---

## Solution



---

## Code
```python
class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    ans = 1
    i = 1
    while i < k:
      gap = self.getGap(ans, ans + 1, n)
      if i + gap <= k:
        i += gap
        ans += 1
      else:
        i += 1
        ans *= 10
    return ans
  def getGap(self, a: int, b: int, n: int) -> int:
    gap = 0
    while a <= n:
      gap += min(n + 1, b) - a
      a *= 10
      b *= 10
    return gap
```