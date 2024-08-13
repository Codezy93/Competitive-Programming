
# Intersection in Two Arrays

Date: 13-08-2024

## Solution
#### Python
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```
        