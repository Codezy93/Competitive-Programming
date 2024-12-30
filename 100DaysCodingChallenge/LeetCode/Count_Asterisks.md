# Count Asterisks

Date: 2024-10-25 12:33:26.225139

## Solution

#### Python
```python
class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        s = [x.count("*") for x in s]
        sum = 0
        for i in range(0, len(s), 2):
            sum += s[i]
        return sum
 ```