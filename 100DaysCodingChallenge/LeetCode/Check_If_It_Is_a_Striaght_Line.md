# Check If It Is a Striaght Line

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prev = 0
        curr = 0
        for i in range(len(coordinates)-1):
            if i == 0:
                try:
                    prev = (coordinates[i][1]-coordinates[i+1][1])/(coordinates[i][0]-coordinates[i+1][0])
                except:
                    prev = inf
            else:
                try:
                    curr = (coordinates[i][1]-coordinates[i+1][1])/(coordinates[i][0]-coordinates[i+1][0])
                except:
                    curr = inf
                if prev != curr:
                    return False
        else:
            return True
 ```