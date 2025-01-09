# 2185. Counting Words With a Given Prefix

---

You are given an array of strings `words` and a string `pref`.

Return _the number of strings in_`words` _that contain_`pref` _as a **prefix **_.

A **prefix ** of a string `s` is any leading contiguous substring of `s`.

 

**Example 1:**


**Input:** words = ["pay","**_at_ ** tention","practice","_ **at **_ tend"], pref = "at"
**Output:** 2
**Explanation:** The 2 strings that contain "at" as a prefix are: "_ **at **_ tention" and "_ **at **_ tend".


**Example 2:**


**Input:** words = ["leetcode","win","loops","success"], pref = "code"
**Output:** 0
**Explanation:** There are no strings that contain "code" as a prefix.


 

**Constraints:**

  * `1 <= words.length <= 100`
  * `1 <= words[i].length, pref.length <= 100`
  * `words[i]` and `pref` consist of lowercase English letters.

---

## Solution



---

## Code
```python
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for i in words:
            if len(i) >= n:
                if i[0:n] == pref:
                    count += 1
        return count
```