# Find the Middle Index in Array

Date: 2024-10-18 00:00:00

## Solution

#### Python
```python
class Solution:
  def findMiddleIndex(self, nums: list[int]) -> int:
    prefix = 0
    suffix = sum(nums)
    for i, num in enumerate(nums):
      suffix -= num
      if prefix == suffix:
        return i
      prefix += num
    return -1
 ```