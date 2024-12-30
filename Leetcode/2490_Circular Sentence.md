# 2490. Circular Sentence

---

A **sentence ** is a list of words that are separated by a **single ** space with no leading or trailing spaces.

  * For example, `"Hello World"`, `"HELLO"`, `"hello world hello world"` are all sentences.



Words consist of **only ** uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is **circular ** if:

  * The last character of each word in the sentence is equal to the first character of its next word.
  * The last character of the last word is equal to the first character of the first word.



For example, `"leetcode exercises sound delightful"`, `"eetcode"`, `"leetcode eats soul" `are all circular sentences. However, `"Leetcode is cool"`, `"happy Leetcode"`, `"Leetcode"` and `"I like Leetcode"` are **not ** circular sentences.

Given a string `sentence`, return `true` _if it is circular_. Otherwise, return `false`.

 

**Example 1:**


**Input:** sentence = "leetcode exercises sound delightful"
**Output:** true
**Explanation:** The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcod _e_ 's last character is equal to _e_ xercises's first character.
- exercise _s_ 's last character is equal to _s_ ound's first character.
- soun _d_ 's last character is equal to _d_ elightful's first character.
- delightfu _l_ 's last character is equal to _l_ eetcode's first character.
The sentence is circular.

**Example 2:**


**Input:** sentence = "eetcode"
**Output:** true
**Explanation:** The words in sentence are ["eetcode"].
- eetcod _e_ 's last character is equal to _e_ etcode's first character.
The sentence is circular.

**Example 3:**


**Input:** sentence = "Leetcode is cool"
**Output:** false
**Explanation:** The words in sentence are ["Leetcode", "is", "cool"].
- Leetcod _e_ 's last character is **not ** equal to _i_ s's first character.
The sentence is **not ** circular.

 

**Constraints:**

  * `1 <= sentence.length <= 500`
  * `sentence` consist of only lowercase and uppercase English letters and spaces.
  * The words in `sentence` are separated by a single space.
  * There are no leading or trailing spaces.

---

## Solution



---

## Code
```python


```