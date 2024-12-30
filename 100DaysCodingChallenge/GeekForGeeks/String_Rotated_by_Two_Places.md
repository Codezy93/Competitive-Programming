
# String Rotated by Two Places

Date: 01-09-2024

## Solution
#### Python
```python
class Solution:
    def isRotated(self,str1,str2):
        if str2[2:]+str2[0:2] == str1:
            return 1
        elif str2[len(str2)-2:]+str2[0:len(str2)-2] == str1:
            return 1
        else:
            return 0
```
        