# 2269. Find the K-Beauty of a Number

---

The **k-beauty ** of an integer `num` is defined as the number of **substrings ** of `num` when it is read as a string that meet the following conditions:

  * It has a length of `k`.
  * It is a divisor of `num`.



Given integers `num` and `k`, return _the k-beauty of_`num`.

Note:

  * **Leading zeros ** are allowed.
  * `0` is not a divisor of any value.



A **substring ** is a contiguous sequence of characters in a string.

 

**Example 1:**


**Input:** num = 240, k = 2
**Output:** 2
**Explanation:** The following are the substrings of num of length k:
- "24" from "**_24_ ** 0": 24 is a divisor of 240.
- "40" from "2 _ **40 **_ ": 40 is a divisor of 240.
Therefore, the k-beauty is 2.


**Example 2:**


**Input:** num = 430043, k = 2
**Output:** 2
**Explanation:** The following are the substrings of num of length k:
- "43" from "_ **43 **_ 0043": 43 is a divisor of 430043.
- "30" from "4 _ **30 **_ 043": 30 is not a divisor of 430043.
- "00" from "43 _ **00 **_ 43": 0 is not a divisor of 430043.
- "04" from "430 _ **04 **_ 3": 4 is not a divisor of 430043.
- "43" from "4300 _ **43 **_ ": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.


 

**Constraints:**

  * `1 <= num <= 109`
  * `1 <= k <= num.length` (taking `num` as a string)

---

## Solution



---

## Code
```python


```