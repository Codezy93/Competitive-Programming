
# Find Highest Altitude

Date: 15-09-2024

## Solution
#### Python
```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain.insert(0, 0)
        max = gain[0]
        sum = 0
        for i in gain:
            sum += i
            if sum > max:
                max = sum
        return max
```
        