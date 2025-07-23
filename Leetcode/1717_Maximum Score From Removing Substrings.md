# 1717. Maximum Score From Removing Substrings

---

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

  * Remove substring `"ab"` and gain `x` points. 
* For example, when removing `"ab"` from `"c _ab_ xbae"` it becomes `"cxbae"`.
  * Remove substring `"ba"` and gain `y` points. 
* For example, when removing `"ba"` from `"cabx _ba_ e"` it becomes `"cabxe"`.



Return _the maximum points you can gain after applying the above operations on_ `s`.

 

**Example 1:**


**Input:** s = "cdbcbbaaabab", x = 4, y = 5
**Output:** 19
**Explanation:**
- Remove the "ba" underlined in "cdbcbbaaa _ba_ b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa _ab_ ". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb _ba_ a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc _ba_ ". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.

**Example 2:**


**Input:** s = "aabbaaxybbaabb", x = 5, y = 4
**Output:** 20


 

**Constraints:**

  * `1 <= s.length <= 105`
  * `1 <= x, y <= 104`
  * `s` consists of lowercase English letters.

---

## Solution



---

## Code
```python
class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    return (self._gain(s, 'ab', x, 'ba', y) if x > y else
            self._gain(s, 'ba', y, 'ab', x))
  def _gain(self, s: str, sub1: str, point1: int, sub2: str, point2: int) -> int:
    points = 0
    stack1 = []
    stack2 = []
    for c in s:
      if stack1 and stack1[-1] == sub1[0] and c == sub1[1]:
        stack1.pop()
        points += point1
      else:
        stack1.append(c)
    for c in stack1:
      if stack2 and stack2[-1] == sub2[0] and c == sub2[1]:
        stack2.pop()
        points += point2
      else:
        stack2.append(c)
    return points
```
