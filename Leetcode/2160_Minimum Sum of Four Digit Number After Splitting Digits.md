# 2160. Minimum Sum of Four Digit Number After Splitting Digits

---

You are given a **positive ** integer `num` consisting of exactly four digits. Split `num` into two new integers `new1` and `new2` by using the **digits ** found in `num`. **Leading zeros ** are allowed in `new1` and `new2`, and **all ** the digits found in `num` must be used.

  * For example, given `num = 2932`, you have the following digits: two `2`'s, one `9` and one `3`. Some of the possible pairs `[new1, new2]` are `[22, 93]`, `[23, 92]`, `[223, 9]` and `[2, 329]`.



Return _the **minimum ** possible sum of _`new1` _and_`new2`.

 

**Example 1:**


**Input:** num = 2932
**Output:** 52
**Explanation:** Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.


**Example 2:**


**Input:** num = 4009
**Output:** 13
**Explanation:** Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.


 

**Constraints:**

  * `1000 <= num <= 9999`

---

## Solution



---

## Code
```python
class Solution:
  def maxTotalFruits(
      self,
      fruits: list[list[int]],
      startPos: int,
      k: int,
  ) -> int:
    ans = 0
    maxRight = max(startPos, fruits[-1][0])
    amounts = [0] * (1 + maxRight)
    for position, amount in fruits:
      amounts[position] = amount
    prefix = list(itertools.accumulate(amounts, initial=0))
    def getFruits(leftSteps: int, rightSteps: int) -> int:
      l = max(0, startPos - leftSteps)
      r = min(maxRight, startPos + rightSteps)
      return prefix[r + 1] - prefix[l]
    for rightSteps in range(min(maxRight - startPos, k) + 1):
      leftSteps = max(0, k - 2 * rightSteps)
      ans = max(ans, getFruits(leftSteps, rightSteps))
    for leftSteps in range(min(startPos, k) + 1):
      rightSteps = max(0, k - 2 * leftSteps)
      ans = max(ans, getFruits(leftSteps, rightSteps))
    return ans
```
