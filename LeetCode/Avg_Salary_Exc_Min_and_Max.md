
# Avg Salary Exc Min and Max

Date: 14-09-2024

## Solution
#### Python
```python
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        return sum(salary[1:-1])/(len(salary)-2)
```
        