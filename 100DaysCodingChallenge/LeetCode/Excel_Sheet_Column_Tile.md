
# Excel Sheet Column Tile

Date: 16-08-2024

## Solution
#### Python
```python
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = []
        while n > 0:
            n -= 1  # Adjust for 0-based indexing
            remainder = n % 26
            result.append(chr(remainder + ord('A')))
            n //= 26
        return ''.join(result[::-1])
```