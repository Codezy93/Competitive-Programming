# 2311. Longest Binary Subsequence Less Than or Equal to K

---

You are given a binary string `s` and a positive integer `k`.

Return _the length of the **longest ** subsequence of _`s` _that makes up a **binary ** number less than or equal to_ `k`.

Note:

  * The subsequence can contain **leading zeroes **.
  * The empty string is considered to be equal to `0`.
  * A **subsequence ** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



 

**Example 1:**


**Input:** s = "1001010", k = 5
**Output:** 5
**Explanation:** The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.


**Example 2:**


**Input:** s = "00101001", k = 1
**Output:** 6
**Explanation:** "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.


 

**Constraints:**

  * `1 <= s.length <= 1000`
  * `s[i]` is either `'0'` or `'1'`.
  * `1 <= k <= 109`

---

## Solution



---

## Code
```python
class Solution:
  def longestSubsequence(self, s: str, k: int) -> int:
    oneCount = 0
    num = 0
    pow = 1
    for i in reversed(range(len(s))):
      if num + pow > k:
        break
      if s[i] == '1':
        oneCount += 1
        num += pow
      pow *= 2
    return s.count('0') + oneCount
```
