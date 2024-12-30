# Greatest of three numbers

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
class Solution:
    def greatestOfThree(self,A,B,C):
        if A > B and A > C:
            return A
        elif B > C and B > A:
            return B
        else:
            return C
 ```