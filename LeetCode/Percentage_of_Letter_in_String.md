# Percentage of Letter in String

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor((s.count(letter)/len(s))*100)
 ```