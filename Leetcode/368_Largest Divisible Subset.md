# 368. Largest Divisible Subset

---

Given a set of **distinct ** positive integers `nums`, return the largest subset `answer` such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

  * `answer[i] % answer[j] == 0`, or
  * `answer[j] % answer[i] == 0`



If there are multiple solutions, return any of them.

 

**Example 1:**


**Input:** nums = [1,2,3]
**Output:** [1,2]
**Explanation:** [1,3] is also accepted.


**Example 2:**


**Input:** nums = [1,2,4,8]
**Output:** [1,2,4,8]


 

**Constraints:**

  * `1 <= nums.length <= 1000`
  * `1 <= nums[i] <= 2 * 109`
  * All the integers in `nums` are **unique **.

---

## Solution



---

## Code
```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        count = [1] * n
        prevIndex = [-1] * n
        maxCount = 0
        index = -1
        nums.sort()
        for i, num in enumerate(nums):
            for j in reversed(range(i)):
                if num % nums[j] == 0 and count[i] < count[j] + 1:
                    count[i] = count[j] + 1
                    prevIndex[i] = j
            if count[i] > maxCount:
                maxCount = count[i]
                index = i
        while index != -1:
            ans.append(nums[index])
            index = prevIndex[index]
        return ans
```