# 916. Word Subsets

---

You are given two string arrays `words1` and `words2`.

A string `b` is a **subset ** of string `a` if every letter in `b` occurs in `a` including multiplicity.

  * For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.



A string `a` from `words1` is **universal ** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal ** strings in `words1`. You may return the answer in **any order **.

 

**Example 1:**

**Input:** words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

**Output:** ["facebook","google","leetcode"]

**Example 2:**

**Input:** words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

**Output:** ["leetcode"]

**Example 3:**

**Input:** words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

**Output:** ["cccbb"]

 

**Constraints:**

  * `1 <= words1.length, words2.length <= 104`
  * `1 <= words1[i].length, words2[i].length <= 10`
  * `words1[i]` and `words2[i]` consist only of lowercase English letters.
  * All the strings of `words1` are **unique **.

---

## Solution



---

## Code
```python
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq_counter = Counter()
        for word in words2:
            word_freq_counter = Counter(word)
            for char, freq in word_freq_counter.items():
                max_freq_counter[char] = max(max_freq_counter[char], freq)
        universal_words = []
        for word in words1:
            word_freq_counter = Counter(word)
            is_universal = all(freq <= word_freq_counter[char] for char, freq in max_freq_counter.items())
            if is_universal:
                universal_words.append(word)
        return universal_words
```