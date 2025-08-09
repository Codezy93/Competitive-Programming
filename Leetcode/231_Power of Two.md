# 231. Power of Two

---

Given an integer `n`, return _`true` if it is a power of two. Otherwise, return `false`_.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

 

**Example 1:**


**Input:** n = 1
**Output:** true
**Explanation:** 20 = 1


**Example 2:**


**Input:** n = 16
**Output:** true
**Explanation:** 24 = 16


**Example 3:**


**Input:** n = 3
**Output:** false


 

**Constraints:**

  * `-231 <= n <= 231 - 1`



 

**Follow up:** Could you solve it without loops/recursion?

---

## Solution

- All the power of two have a pattern in binary format that the left most bit is a set bit and others are unset bits.

1 = 1
2 = 10
4 = 100
8 = 1000
16 = 10000

- So basically we write a code to convert the integer to binary format.
- Check if the left most bit is set and check if all other bits are unset.
---

## Code
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        n = bin(n).replace("0b", "")
        return n[0] == '1' and int(n[1:]) == 0
```
