# Number is sparse or not

Date: 2024-10-06 19:39:58.074223

## Solution

#### Python
```python
class Solution:
    def isSparse(self,n):
        n = bin(n).replace("0b", "")
        if "11" in n:
            return 0
        else:
            return 1
 ```