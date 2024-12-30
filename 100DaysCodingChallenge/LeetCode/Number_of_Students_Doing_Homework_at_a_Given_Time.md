
# Number of Students Doing Homework at a Given Time

Date: 28-08-2024

## Solution
#### Python
```python
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i, j in enumerate(startTime):
            if queryTime >= j and queryTime <= endTime[i]:
                count += 1
        return count
```
        