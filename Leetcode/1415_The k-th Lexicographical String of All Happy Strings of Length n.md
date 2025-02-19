# 1415. The k-th Lexicographical String of All Happy Strings of Length n

---

A **happy string ** is a string that:

  * consists only of letters of the set `['a', 'b', 'c']`.
  * `s[i] != s[i + 1]` for all values of `i` from `1` to `s.length - 1` (string is 1-indexed).



For example, strings **" abc", "ac", "b"** and **" abcbabcbcb"** are all happy strings and strings **" aa", "baa"** and **" ababbc"** are not happy strings.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order.

Return _the kth string_ of this list or return an **empty string ** if there are less than `k` happy strings of length `n`.

 

**Example 1:**


**Input:** n = 1, k = 3
**Output:** "c"
**Explanation:** The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".


**Example 2:**


**Input:** n = 1, k = 4
**Output:** ""
**Explanation:** There are only 3 happy strings of length 1.


**Example 3:**


**Input:** n = 3, k = 9
**Output:** "cab"
**Explanation:** There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"


 

**Constraints:**

  * `1 <= n <= 10`
  * `1 <= k <= 100`

---

## Solution



---

## Code
```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(current_str):
            if len(current_str) == n:
                happy_strings.append(current_str)
                return
            for char in 'abc':
                if current_str and current_str[-1] == char:
                    continue
                dfs(current_str + char)
        happy_strings = []
        dfs('')
        return '' if len(happy_strings) < k else happy_strings[k - 1]
```