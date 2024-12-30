# Find Digits

Date: 2024-10-05 00:00:00

## Solution

#### Python
```python
def findDigits(n):
    steps = 0
    for i in str(n):
        if i == "0":
            pass
        elif n%int(i) == 0:
            steps += 1
        else:
            pass          
    return steps
 ```