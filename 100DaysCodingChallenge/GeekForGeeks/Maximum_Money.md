# Maximum Money

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
class Solution:
    def maximizeMoney(self, N , K):
        if N%2 == 0:
            return (N//2)*K
        else:
            return ((N//2)+1)*K
 ```