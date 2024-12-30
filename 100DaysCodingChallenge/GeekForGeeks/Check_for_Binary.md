
# Check for Binary

Date: 27-09-2024

## Solution
#### Python
```python
def isBinary(str):
    for i in str:
        if i not in ["1", "0"]:
            return 0
    else:
        return 1
```
        