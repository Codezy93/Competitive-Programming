# Chocolate Feast

Date: 2024-10-14 10:16:05.314276

## Solution

#### Python
```python
def chocolateFeast(n, c, m):
    chocolates = n//c
    wrappers = n//c
    while wrappers >= m:
        chocolates += 1
        wrappers -= m
        wrappers += 1
    return chocolates
 ```