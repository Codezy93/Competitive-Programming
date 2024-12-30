# Count items matching rule

Date: 2024-10-21 00:00:00

## Solution

#### Python
```python
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2
        count = 0
        for i in items:
            if i[index] == ruleValue:
                count += 1
        return count
 ```