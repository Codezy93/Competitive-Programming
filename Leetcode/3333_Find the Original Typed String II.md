# 3333. Find the Original Typed String II

---

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may ** press a key for too long, resulting in a character being typed **multiple ** times.

You are given a string `word`, which represents the **final ** output displayed on Alice's screen. You are also given a **positive ** integer `k`.

Return the total number of _possible_ original strings that Alice _might_ have intended to type, if she was trying to type a string of size **at least ** `k`.

Since the answer may be very large, return it **modulo ** `109 + 7`.

 

**Example 1:**

**Input:** word = "aabbccdd", k = 7

**Output:** 5

**Explanation:**

The possible strings are: `"aabbccdd"`, `"aabbccd"`, `"aabbcdd"`, `"aabccdd"`, and `"abbccdd"`.

**Example 2:**

**Input:** word = "aabbccdd", k = 8

**Output:** 1

**Explanation:**

The only possible string is `"aabbccdd"`.

**Example 3:**

**Input:** word = "aaabbb", k = 3

**Output:** 8

 

**Constraints:**

  * `1 <= word.length <= 5 * 105`
  * `word` consists only of lowercase English letters.
  * `1 <= k <= 2000`

---

## Solution



---

## Code
```python
class Solution:
  def possibleStringCount(self, word: str, k: int) -> int:
    MOD = 1_000_000_007
    groups = self._getConsecutiveLetters(word)
    totalCombinations = functools.reduce(lambda subtotal, group:
                                         subtotal * group % MOD, groups)
    if k <= len(groups):
      return totalCombinations
    dp = [0] * k
    dp[0] = 1
    for i, group in enumerate(groups):
      newDp = [0] * k
      windowSum = 0
      for j in range(i, k):
        newDp[j] = (newDp[j] + windowSum) % MOD
        windowSum = (windowSum + dp[j]) % MOD
        if j >= group:
          windowSum = (windowSum - dp[j - group] + MOD) % MOD
      dp = newDp
    return (totalCombinations - sum(dp)) % MOD
  def _getConsecutiveLetters(self, word: str) -> list[int]:
    groups = []
    group = 1
    for i in range(1, len(word)):
      if word[i] == word[i - 1]:
        group += 1
      else:
        groups.append(group)
        group = 1
    groups.append(group)
    return groups
```
