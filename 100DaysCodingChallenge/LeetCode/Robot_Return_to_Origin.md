
# Robot Return to Origin

Date: 04-09-2024

## Solution
#### Python
```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x,y = 0,0
        for i in moves:
            if i == "L":
                x -= 1
            elif i == "R":
                x += 1
            elif i == "U":
                y += 1
            else:
                y -= 1
        return x == 0 and y == 0
```
        