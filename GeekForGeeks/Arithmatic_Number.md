# Arithmatic Number

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
class Solution:
    def inSequence(self, A, B, C):
        if C == 0:
            if A==B:
                return 1
            else:
                return 0
        return 1 if ((B-A)/C)==abs(((B-A)//C)) else 0
 ```