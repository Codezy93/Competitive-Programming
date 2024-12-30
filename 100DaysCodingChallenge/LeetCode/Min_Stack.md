# Min Stack

Date: 2024-10-28 00:00:00

## Solution

#### Python
```python
class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.insert(0, val)
    def pop(self) -> None:
        del self.stack[0]
    def top(self) -> int:
        return self.stack[0]
    def getMin(self) -> int:
        return min(self.stack)
 ```