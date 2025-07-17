# 3202. Find the Maximum Length of Valid Subsequence II

---

You are given an integer array `nums` and a **positive ** integer `k`. 

A subsequence `sub` of `nums` with length `x` is called **valid ** if it satisfies:

  * `(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.`

Return the length of the **longest ** **valid ** subsequence of `nums`. 

 

**Example 1:**

**Input:** nums = [1,2,3,4,5], k = 2

**Output:** 5

**Explanation:**

The longest valid subsequence is `[1, 2, 3, 4, 5]`.

**Example 2:**

**Input:** nums = [1,4,2,3,1,4], k = 3

**Output:** 4

**Explanation:**

The longest valid subsequence is `[1, 4, 1, 4]`.

 

**Constraints:**

  * `2 <= nums.length <= 103`
  * `1 <= nums[i] <= 107`
  * `1 <= k <= 103`

---

## Solution



---

## Code
```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        count_matrix = [[0] * k for _ in range(k)]
        max_length = 0
        for num in nums:
            remainder = num % k
            for j in range(k):
                complement_remainder = (j - remainder + k) % k
                count_matrix[remainder][complement_remainder] = count_matrix[complement_remainder][remainder] + 1
                max_length = max(max_length, count_matrix[remainder][complement_remainder])
        return max_length
```
