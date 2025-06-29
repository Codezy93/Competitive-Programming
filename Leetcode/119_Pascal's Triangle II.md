# 119. Pascal's Triangle II

---

Given an integer `rowIndex`, return the `rowIndexth` (**0-indexed **) row of the **Pascal 's triangle **.

In **Pascal 's triangle **, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

 

**Example 1:**


**Input:** rowIndex = 3
**Output:** [1,3,3,1]


**Example 2:**


**Input:** rowIndex = 0
**Output:** [1]


**Example 3:**


**Input:** rowIndex = 1
**Output:** [1,1]


 

**Constraints:**

  * `0 <= rowIndex <= 33`



 

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?

---

## Solution



---

## Code
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1, 1]
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex-1):
            temp = []
            temp.append(row[0])
            for j in range(len(row)-1):
                temp.append(row[j]+row[j+1])
            temp.append(row[-1])
            row = temp
        return row
```