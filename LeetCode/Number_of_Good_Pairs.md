# Number of Good Pairs

Date: 2024-11-02 00:00:00

## Solution

#### Python
```python
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    count += 1
        return count
 ```