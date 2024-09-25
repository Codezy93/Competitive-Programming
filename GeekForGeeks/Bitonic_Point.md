
# Bitonic Point

Date: 25-09-2024

## Solution
#### Python
```python
class Solution:
	def findMaximum(self,arr, n):
		for i in range(0, n-1):
		    if arr[i] > arr[i+1]:
		        return arr[i]
		else:
		    return arr[-1]
```
        