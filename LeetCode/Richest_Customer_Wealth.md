
# Richest Customer Wealth

Date: 24-08-2024

## Solution
#### Python
```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum += j
            if sum > max:
                max = sum
        return max
```
        