# 1358. Number of Substrings Containing All Three Characters

---

Given a string `s` consisting only of characters _a_ , _b_ and _c_.

Return the number of substrings containing **at least **  one occurrence of all these characters _a_ , _b_ and _c_.

 

**Example 1:**


**Input:** s = "abcabc"
**Output:** 10
**Explanation:** The substrings containing at least one occurrence of the characters _a_ , _b_  and _c are "_abc _" , "_abca _" , "_abcab _" , "_abcabc _" , "_bca _" , "_bcab _" , "_bcabc _" , "_cab _" , "_cabc _" _and _ "_abc _" _(**again **)_._


**Example 2:**


**Input:** s = "aaacb"
**Output:** 3
**Explanation:** The substrings containing at least one occurrence of the characters _a_ , _b_  and _c are "_aaacb _" , "_aacb _" _and _ "_acb _".___


**Example 3:**


**Input:** s = "abc"
**Output:** 1


 

**Constraints:**

  * `3 <= s.length <= 5 x 10^4`
  * `s` only consists of _a_ , _b_ or _c  _characters.

---

## Solution



---

## Code
```python
class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    ans = 0
    lastSeen = {c: -1 for c in 'abc'}
    for i, c in enumerate(s):
      lastSeen[c] = i
      ans += 1 + min(lastSeen.values())
    return ans
```