# Sum of AP Series

Date: 2024-10-31 00:00:00

## Solution

#### Python
```python
class Solution:
    def sum_of_ap(self, n, a, d):
        s = (n/2)*(a + a + ((n-1)*d))
        return int(s)
 ```