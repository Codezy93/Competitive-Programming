# 2099. Find Subsequence of Length K With the Largest Sum

---

You are given an integer array `nums` and an integer `k`. You want to find a **subsequence ** of `nums` of length `k` that has the **largest ** sum.

Return ___ **any ** such subsequence as an integer array of length _`k`.

A **subsequence ** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

**Example 1:**


**Input:** nums = [2,1,3,3], k = 2
**Output:** [3,3]
**Explanation:**
The subsequence has the largest sum of 3 + 3 = 6.

**Example 2:**


**Input:** nums = [-1,-2,3,4], k = 3
**Output:** [-1,3,4]
**Explanation:** 
The subsequence has the largest sum of -1 + 3 + 4 = 6.


**Example 3:**


**Input:** nums = [3,4,3,3], k = 2
**Output:** [3,4]
**Explanation:**
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].


 

**Constraints:**

  * `1 <= nums.length <= 1000`
  * `-105 <= nums[i] <= 105`
  * `1 <= k <= nums.length`

---

## Solution



---

## Code
```python
class Solution:
  def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
    ans = []
    threshold = sorted(nums)[-k]
    larger = sum(num > threshold for num in nums)
    equal = k - larger
    for num in nums:
      if num > threshold:
        ans.append(num)
      elif num == threshold and equal:
        ans.append(num)
        equal -= 1
    return ans
```
