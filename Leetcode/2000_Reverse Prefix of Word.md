# 2000. Reverse Prefix of Word

---

Given a **0-indexed ** string `word` and a character `ch`, **reverse ** the segment of `word` that starts at index `0` and ends at the index of the **first occurrence ** of `ch` (**inclusive **). If the character `ch` does not exist in `word`, do nothing.

  * For example, if `word = "abcdefd"` and `ch = "d"`, then you should **reverse ** the segment that starts at `0` and ends at `3` (**inclusive **). The resulting string will be `"_dcba_ efd"`.



Return _the resulting string_.

 

**Example 1:**


**Input:** word = "_abcd_ efd", ch = "d"
**Output:** "_dcba_ efd"
**Explanation:**  The first occurrence of "d" is at index 3. 
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".


**Example 2:**


**Input:** word = "_xyxz_ xe", ch = "z"
**Output:** "_zxyx_ xe"
**Explanation:**  The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".


**Example 3:**


**Input:** word = "abcd", ch = "z"
**Output:** "abcd"
**Explanation:**  "z" does not exist in word.
You should not do any reverse operation, the resulting string is "abcd".


 

**Constraints:**

  * `1 <= word.length <= 250`
  * `word` consists of lowercase English letters.
  * `ch` is a lowercase English letter.

---

## Solution



---

## Code
```python
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        return word[:idx+1][::-1] + word[idx+1:]
```