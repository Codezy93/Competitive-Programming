
# Excel Sheet Column Number

Date: 07-09-2024

## Solution
#### Python
```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char.upper()) - ord('A') + 1)
        return result
```
        