# Find lucky integer in array

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        map = {}
        for i in arr:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        count = -1
        for i in map:
            if map[i] == i and count < i:
                count = i
        return count
 ```