
# Value equal Index

Date: 17-09-2024

## Solution
#### Python
```python
class Solution:
    def valueEqualToIndex(self, arr):
        a = []
        for i, j in enumerate(arr):
            if i+1 == j:
                a.append(i+1)
        return a
```
        