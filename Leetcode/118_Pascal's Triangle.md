# 118. Pascal's Triangle

---

Given an integer `numRows`, return the first numRows of **Pascal 's triangle **.

In **Pascal 's triangle **, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

 

**Example 1:**


**Input:** numRows = 5
**Output:** [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


**Example 2:**


**Input:** numRows = 1
**Output:** [[1]]


 

**Constraints:**

  * `1 <= numRows <= 30`

---

## Solution



---

## Code
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
