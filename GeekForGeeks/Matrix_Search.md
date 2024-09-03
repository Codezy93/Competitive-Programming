
# Matrix Search

Date: 03-09-2024

## Solution
#### Python
```python
class Solution:
	def matSearch(self,mat, N, M, X):
		for i in mat:
		    for j in i:
		        if j == X:
		            return 1
		else:
		    return 0
```
        