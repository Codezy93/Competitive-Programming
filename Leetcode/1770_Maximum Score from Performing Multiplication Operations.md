# 1770. Maximum Score from Performing Multiplication Operations

---

You are given two **0-indexed ** integer arrays `nums` and `multipliers`**** of size `n` and `m` respectively, where `n >= m`.

You begin with a score of `0`. You want to perform **exactly ** `m` operations. On the `ith` operation (**0-indexed **) you will:

  * Choose one integer `x` from **either the start or the end ** of the array `nums`.
  * Add `multipliers[i] * x` to your score. 
* Note that `multipliers[0]` corresponds to the first operation, `multipliers[1]` to the second operation, and so on.
  * Remove `x` from `nums`.



Return _the **maximum ** score after performing _`m` _operations._

 

**Example 1:**


**Input:** nums = [1,2,3], multipliers = [3,2,1]
**Output:** 14
**Explanation:**  An optimal solution is as follows:
- Choose from the end, [1,2,**_3_ **], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,**_2_ **], adding 2 * 2 = 4 to the score.
- Choose from the end, [**_1_ **], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.

**Example 2:**


**Input:** nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
**Output:** 102
**Explanation:** An optimal solution is as follows:
- Choose from the start, [_ **-5 **_ ,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [**_-3_ ** ,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [**_-3_ ** ,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,**_1_ **], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,**_7_ **], adding 7 * 6 = 42 to the score. 
The total score is 50 + 15 - 9 + 4 + 42 = 102.


 

**Constraints:**

  * `n == nums.length`
  * `m == multipliers.length`
  * `1 <= m <= 300`
  * `m <= n <= 105`` `
  * `-1000 <= nums[i], multipliers[i] <= 1000`

---

## Solution



---

## Code
```python


```