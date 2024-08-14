
# Finding Smallest Letter Greater than Target

Date: 14-08-2024

## Solution
#### Python
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = letters[0]
        letters.sort()
        for i in letters:
            if i > target:
                return i
        else:
            return start
```
        