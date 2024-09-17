
# Pascals Triangle

Date: 17-09-2024

## Solution
#### Python
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        pascal = [[1], [1, 1]]
        for i in range(numRows-2):
            temp = []
            temp.append(pascal[-1][0])
            temp.append(pascal[-1][-1])
            for j, k in enumerate(pascal[-1]):
                if j != len(pascal[-1])-1:
                    temp.insert(-1, k+pascal[-1][j+1])
            pascal.append(temp)
        return pascal
```
        