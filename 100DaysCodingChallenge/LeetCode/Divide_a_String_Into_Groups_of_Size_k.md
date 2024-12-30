# Divide a String Into Groups of Size k

Date: 2024-11-01 00:00:00

## Solution

#### Python
```python
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = [s[i:i+k] for i in range(0, len(s), k)]
        if len(s[-1]) != k:
            s[-1] = s[-1] + fill*(k-len(s[-1]))
        return s
 ```