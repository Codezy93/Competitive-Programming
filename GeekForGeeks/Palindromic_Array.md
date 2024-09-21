
# Palindromic Array

Date: 21-09-2024

## Solution
#### Python
```python
def palin(string):
    if len(string)%2 == 0:
        if string == string[::-1]:
            return True
        else:
            return False
    else:
        if string == string[::-1]:
            return True
        else:
            return False
def PalinArray(arr):
    for i in arr:
        if not palin(str(i)):
            return False
    else:
        return True
```
        