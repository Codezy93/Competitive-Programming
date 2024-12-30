# Cells in a Range on an Excel Sheet

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        A, B, C ,D = list(s.replace(":", ""))
        res = []
        for i in range(ord(A), ord(C)+1):
            for j in range(int(B), int(D)+1):
                res.append(f"{chr(i)}{j}")
        return res
 ```