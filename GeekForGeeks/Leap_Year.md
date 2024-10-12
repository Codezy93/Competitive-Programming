# Leap Year

Date: 2024-10-12 18:03:23.457274

## Solution

#### Python
```python
class Solution:
    def isLeap (self, N):
        return 1 if (N%4==0 and N%100!=0) or N%400==0 else 0
 ```