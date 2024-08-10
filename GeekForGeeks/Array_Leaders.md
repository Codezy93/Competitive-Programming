
# Array Leaders

Date: 10-08-2024

## Solution
#### Python
```python
class Solution:
    def leaders(self,n, arr):
        leaders = []
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    break
            else:
                leaders.append(arr[i])
        return leaders
```
        