# 416. Partition Equal Subset Sum

---

Given an integer array `nums`, return `true` _if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or_`false` _otherwise_.

 

**Example 1:**


**Input:** nums = [1,5,11,5]
**Output:** true
**Explanation:** The array can be partitioned as [1, 5, 5] and [11].


**Example 2:**


**Input:** nums = [1,2,3,5]
**Output:** false
**Explanation:** The array cannot be partitioned into equal sum subsets.


 

**Constraints:**

  * `1 <= nums.length <= 200`
  * `1 <= nums[i] <= 100`

---

## Solution



---

## Code
```python
class Solution:
  def canPartition(self, nums: list[int]) -> bool:
    summ = sum(nums)
    if summ % 2 == 1:
      return False
    return self.knapsack_(nums, summ // 2)
  def knapsack_(self, nums: list[int], subsetSum: int) -> bool:
    n = len(nums)
    dp = [[False] * (subsetSum + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
      num = nums[i - 1]
      for j in range(subsetSum + 1):
        if j < num:
          dp[i][j] = dp[i - 1][j]
        else:
          dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
    return dp[n][subsetSum]
```