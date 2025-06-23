# 520. Detect Capital

---

We define the usage of capitals in a word to be right when one of the following cases holds:

  * All letters in this word are capitals, like `"USA"`.
  * All letters in this word are not capitals, like `"leetcode"`.
  * Only the first letter in this word is capital, like `"Google"`.



Given a string `word`, return `true` if the usage of capitals in it is right.

 

**Example 1:**


**Input:** word = "USA"
**Output:** true


**Example 2:**


**Input:** word = "FlaG"
**Output:** false


 

**Constraints:**

  * `1 <= word.length <= 100`
  * `word` consists of lowercase and uppercase English letters.

---

## Solution



---

## Code
```python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u, l = 0, 0
        for i in word:
            if i.isupper():
                u += 1
            else:
                l += 1
        if u == len(word) or l == len(word):
            return True
        else:
            if word[0].isupper() and l == len(word)-1:
                return True
            else:
                return False
```
