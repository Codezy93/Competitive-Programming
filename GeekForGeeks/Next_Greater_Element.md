
# Next Greater Element

Date: 13-08-2024

## Solution
#### Python
```python
class Solution:
    def nextLargerElement(self, arr, n):
        out = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                out[stack.pop()] = arr[i]
            stack.append(i)
        return out
```
        