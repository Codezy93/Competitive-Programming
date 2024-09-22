
# Kids With the Greatest Number of Candies

Date: 22-09-2024

## Solution
#### Python
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        for i, j in enumerate(candies):
            if j+extraCandies >= m:
                candies[i] = True
            else:
                candies[i] = False
        return candies
```
        