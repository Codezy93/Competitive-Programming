
# Find the median

Date: 12-08-2024

## Solution
#### Python
```python
class Solution:
	def find_median(self, v):
	    v.sort()
		mid = len(v) // 2
        res = (v[mid] + v[~mid]) / 2
        return int(res)
```
        