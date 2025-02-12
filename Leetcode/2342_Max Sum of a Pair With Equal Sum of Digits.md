# 2342. Max Sum of a Pair With Equal Sum of Digits

---

You are given a **0-indexed ** array `nums` consisting of **positive ** integers. You can choose two indices `i` and `j`, such that `i != j`, and the sum of digits of the number `nums[i]` is equal to that of `nums[j]`.

Return _the **maximum ** value of _`nums[i] + nums[j]`_that you can obtain over all possible indices_`i` _and_`j` _that satisfy the conditions._

 

**Example 1:**


**Input:** nums = [18,43,36,13,7]
**Output:** 54
**Explanation:** The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.


**Example 2:**


**Input:** nums = [10,12,19,14]
**Output:** -1
**Explanation:** There are no two numbers that satisfy the conditions, so we return -1.


 

**Constraints:**

  * `1 <= nums.length <= 105`
  * `1 <= nums[i] <= 109`

---

## Solution



---

## Code
```python
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sums = {}
        for i in nums:
            temp = 0
            for j in str(i):
                temp += int(j)
            if temp in sums:
                sums[temp].append(i)
            else:
                sums[temp] = [i]
        max_sum = -1
        for i in sums:
            if len(sums[i]) == 1:
                pass
            elif len(sums[i]) == 2:
                if max_sum < sums[i][0] + sums[i][1]:
                    max_sum = sums[i][0] + sums[i][1]
            else:
                m1 = 0
                m2 = 0
                for j in sums[i]:
                    if j > m1:
                        m2 = m1
                        m1 = j
                    elif j > m2:
                        m2 = j
                    else:
                        pass
                if m1+m2 > max_sum:
                    max_sum = m1+m2
        return max_sum
```