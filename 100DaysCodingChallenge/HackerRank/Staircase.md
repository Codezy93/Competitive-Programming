# Staircase

Date: 2024-10-29 00:00:00

## Solution

#### Python
```python
def staircase(n):
    index = 2
    for i in range(1, n+1):
        a = " "*(n-i) + "#"*i
        print(a)
 ```