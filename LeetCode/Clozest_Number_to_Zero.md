# Clozest Number to Zero

Date: 2024-11-04 00:00:00

## Solution

#### Python
```python
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_val = float('inf')
        val = -1*float('inf')
        for i in nums:
            if abs(i) < min_val:
                min_val = abs(i)
                val = i
            elif abs(i) == min_val:
                if val < i:
                    val = i
            else:
                pass
        return val
 ```