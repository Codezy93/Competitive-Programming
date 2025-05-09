# 2962. Count Subarrays Where Max Element Appears at Least K Times

---

You are given an integer array `nums` and a **positive ** integer `k`.

Return _the number of subarrays where the **maximum ** element of _`nums` _appears **at least ** _`k` _times in that subarray._

A **subarray ** is a contiguous sequence of elements within an array.

 

**Example 1:**


**Input:** nums = [1,3,2,3,3], k = 2
**Output:** 6
**Explanation:** The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].


**Example 2:**


**Input:** nums = [1,4,2,1], k = 3
**Output:** 0
**Explanation:** No subarray contains the element 4 at least 3 times.


 

**Constraints:**

  * `1 <= nums.length <= 105`
  * `1 <= nums[i] <= 106`
  * `1 <= k <= 105`

---

## Solution



---

## Code
```python
class Solution:
  def countSubarrays(self, nums: list[int], k: int) -> int:
    maxNum = max(nums)
    ans = 0
    count = 0
    l = 0
    for r, num in enumerate(nums):
      if num == maxNum:
        count += 1
      while count == k:
        if nums[l] == maxNum:
          count -= 1
        l += 1
      ans += l
    return ans
```