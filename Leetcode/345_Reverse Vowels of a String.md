# 345. Reverse Vowels of a String

---

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

 

**Example 1:**

**Input:** s = "IceCreAm"

**Output:** "AceCreIm"

**Explanation:**

The vowels in `s` are `['I', 'e', 'e', 'A']`. On reversing the vowels, s becomes `"AceCreIm"`.

**Example 2:**

**Input:** s = "leetcode"

**Output:** "leotcede"

 

**Constraints:**

  * `1 <= s.length <= 3 * 105`
  * `s` consist of **printable ASCII ** characters.

---

## Solution



---

## Code
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            return c in "aeiouAEIOU"
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            if isVowel(s[left]) == False:
                left += 1
            if isVowel(s[right]) == False:
                right -= 1
            if isVowel(s[left]) and isVowel(s[right]):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        s = "".join(s)
        return s
```
