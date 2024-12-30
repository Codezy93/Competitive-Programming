
# Goal Parser Interpretation

Date: 28-09-2024

## Solution
#### Python
```python
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(", "")
        command = command.replace(")", "")
        return command
```
        