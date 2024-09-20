
# Crawler Log Folder

Date: 20-09-2024

## Solution
#### Python
```python
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i, j in enumerate(logs):
            if j == "../" and i != 0 and count != 0:
                count -= 1
            elif j == "../" and logs[i-1] == "../" and i != 0:
                count = 0
            elif j != "../" and j != "./":
                count += 1
            else:
                pass
        return count
```
        