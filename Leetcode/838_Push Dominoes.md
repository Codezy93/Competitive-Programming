# 838. Push Dominoes

---

There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string `dominoes` representing the initial state where:

  * `dominoes[i] = 'L'`, if the `ith` domino has been pushed to the left,
  * `dominoes[i] = 'R'`, if the `ith` domino has been pushed to the right, and
  * `dominoes[i] = '.'`, if the `ith` domino has not been pushed.



Return _a string representing the final state_.

 

**Example 1:**


**Input:** dominoes = "RR.L"
**Output:** "RR.L"
**Explanation:** The first domino expends no additional force on the second domino.


**Example 2:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png)


**Input:** dominoes = ".L.R...LR..L.."
**Output:** "LL.RR.LLRRLL.."


 

**Constraints:**

  * `n == dominoes.length`
  * `1 <= n <= 105`
  * `dominoes[i]` is either `'L'`, `'R'`, or `'.'`.

---

## Solution



---

## Code
```python
class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    ans = list(dominoes)
    L = -1
    R = -1
    for i in range(len(dominoes) + 1):
      if i == len(dominoes) or dominoes[i] == 'R':
        if L < R:
          while R < i:
            ans[R] = 'R'
            R += 1
        R = i
      elif dominoes[i] == 'L':
        if R < L or (L, R) == (-1, -1):
          if (L, R) == (-1, -1):
            L += 1
          while L < i:
            ans[L] = 'L'
            L += 1
        else:
          l = R + 1
          r = i - 1
          while l < r:
            ans[l] = 'R'
            ans[r] = 'L'
            l += 1
            r -= 1
        L = i
    return ''.join(ans)
```