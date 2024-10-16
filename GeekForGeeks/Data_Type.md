# Data Type

Date: 2024-10-16 17:49:38.584114

## Solution

#### Python
```python
class Solution:
    def dataTypeSize(self, str):
        if str == "Character":
            return 1
        elif str == "Integer":
            return 4
        elif str == "Long":
            return 8
        elif str == "Float":
            return 4
        elif str == "Double":
            return 8
        else:
            return -1
 ```