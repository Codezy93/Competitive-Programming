# 905. Sort Array By Parity

---

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return _ **any array ** that satisfies this condition_.

 

**Example 1:**


**Input:** nums = [3,1,2,4]
**Output:** [2,4,3,1]
**Explanation:** The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


**Example 2:**


**Input:** nums = [0]
**Output:** [0]


 

**Constraints:**

  * `1 <= nums.length <= 5000`
  * `0 <= nums[i] <= 5000`

---

## Solution



---

## Code
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l]%2==1 and nums[r]%2==0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            else:
                if nums[l]%2==0:
                    l+=1
                if nums[r]%2!=0:
                    r-=1
        return nums
```
