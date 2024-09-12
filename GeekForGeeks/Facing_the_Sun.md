
# Facing the Sun

Date: 12-09-2024

## Solution
#### Python
```python
class Solution:
    def countBuildings(self, height):
        max = height[0]-1
        count = 0
        for i in height:
            if i > max:
                count += 1
                max = i
        return count
```
        