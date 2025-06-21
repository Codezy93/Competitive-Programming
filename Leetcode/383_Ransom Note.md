# 383. Ransom Note

---

Given two strings `ransomNote` and `magazine`, return `true` _if_`ransomNote` _can be constructed by using the letters from_`magazine` _and_`false` _otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

 

**Example 1:**


**Input:** ransomNote = "a", magazine = "b"
**Output:** false


**Example 2:**


**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false


**Example 3:**


**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true


 

**Constraints:**

  * `1 <= ransomNote.length, magazine.length <= 105`
  * `ransomNote` and `magazine` consist of lowercase English letters.

---

## Solution



---

## Code
```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def hasher(l):
            map = {}
            for i in l:
                if i in map:
                    map[i] += 1
                else:
                    map[i] = 1
            return map
        m = hasher(magazine)
        r = hasher(ransomNote)
        for i in r:
            if i not in m or r[i] > m[i]:
                return False
        return True
```
