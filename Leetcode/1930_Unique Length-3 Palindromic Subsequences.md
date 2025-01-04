# 1930. Unique Length-3 Palindromic Subsequences

---

Given a string `s`, return _the number of **unique palindromes of length three ** that are a **subsequence ** of _`s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once **.

A **palindrome ** is a string that reads the same forwards and backwards.

A **subsequence ** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

  * For example, `"ace"` is a subsequence of `"_a_ b _c_ d _e_ "`.



 

**Example 1:**


**Input:** s = "aabca"
**Output:** 3
**Explanation:** The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "_a_ a _b_ c _a_ ")
- "aaa" (subsequence of "_aa_ bc _a_ ")
- "aca" (subsequence of "_a_ ab _ca_ ")


**Example 2:**


**Input:** s = "adc"
**Output:** 0
**Explanation:** There are no palindromic subsequences of length 3 in "adc".


**Example 3:**


**Input:** s = "bbcbaba"
**Output:** 4
**Explanation:** The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "_bb_ c _b_ aba")
- "bcb" (subsequence of "_b_ b _cb_ aba")
- "bab" (subsequence of "_b_ bcb _ab_ a")
- "aba" (subsequence of "bbcb _aba_ ")


 

**Constraints:**

  * `3 <= s.length <= 105`
  * `s` consists of only lowercase English letters.

---

## Solution



---

## Code
```python
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
        first_index = {}
        last_index = {}
        for i in range(len(s)):
            if s[i] not in first_index:
                first_index[s[i]] = i
            last_index[s[i]] = i
        for c in first_index:
            if first_index[c] < last_index[c]:
                for char_between in set(s[first_index[c]+1:last_index[c]]):
                    unique_palindromes.add((c, char_between, c))
        return len(unique_palindromes)
```