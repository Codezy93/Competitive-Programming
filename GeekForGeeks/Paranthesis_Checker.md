# Paranthesis Checker

Date: 2024-10-11 00:00:00

## Solution

#### Python
```python
class Solution:
    def ispar(self,arr):
        arr = list(arr)
        stack = []
        for i in arr:
            if i in "[{(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if i == "}":
                        if stack[-1] == "{":
                            del stack[-1]
                        else:
                            return False
                    elif i == "]":
                        if stack[-1] == "[":
                            del stack[-1]
                        else:
                            return False
                    elif i == ")":
                        if stack[-1] == "(":
                            del stack[-1]
                        else:
                            return False
                    else:
                        pass
        if len(stack) == 0:
            return True
        else:
            return False
 ```