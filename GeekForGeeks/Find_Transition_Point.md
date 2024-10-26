# Find Transition Point

Date: 2024-10-26 18:21:47.060623

## Solution

#### Python
```python
class Solution:
    def transitionPoint(self, arr): 
        return arr.index(1) if 1 in arr else -1
 ```