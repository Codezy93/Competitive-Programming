
# Plus One

Date: 08-09-2024

## Solution
#### Python
```python
class Solution:
    def increment(self, arr, N):
        arr = list(map(int, arr))
        carry = 1
        for i in range(N - 1, -1, -1):
            arr[i] += carry
            if arr[i] == 10:
                arr[i] = 0
                carry = 1
            else:
                carry = 0
                break
        if carry == 1:
            arr.insert(0, 1)
        return " ".join(map(str, arr))
```
        