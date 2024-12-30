# Remove Trailing Zeros From a String

Date: 2024-11-07 00:00:00

## Solution

#### Python
```python
class Solution:
    def removeTrailingZeros(self, nums: str) -> str:
        nums = list(nums)
        while nums[-1] == "0":
            del nums[-1]
        return "".join(nums)
 ```