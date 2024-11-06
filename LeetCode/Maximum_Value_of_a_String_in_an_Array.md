# Maximum Value of a String in an Array

Date: 2024-11-06 00:00:00

## Solution

#### Python
```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = -1
        for i in strs:
            try:
                temp = int(i)
                if temp > max_val:
                    max_val = temp
            except:
                if len(i) > max_val:
                    max_val = len(i)
        return max_val
 ```