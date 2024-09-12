
# Thousand Seperator

Date: 12-09-2024

## Solution
#### Python
```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        return f'{n:,}'.replace(",", ".")
```
        