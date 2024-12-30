
# Print 1 to n without loop

Date: 01-10-2024

## Solution
#### Python
```python
class Solution:
    def printTillN(self, N):
    	if N == 0:
    	    return 1
    	else:
    	    self.printTillN(N-1)
    	    print(N, end = " ")
```
        