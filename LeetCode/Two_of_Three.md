# Two of Three

Date: 2024-10-13 19:26:26.421996

## Solution

#### Python
```python
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all = set(nums1+nums2+nums3)
        out = []
        for i in all:
            temp = 0
            if i in nums1:
                temp += 1
            if i in nums2:
                temp += 1
            if i in nums3:
                temp += 1
            if temp >= 2:
                out.append(i)
        return out
 ```