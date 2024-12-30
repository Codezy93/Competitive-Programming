# Vasya and Hipster

Date: 2024-10-06 19:39:58.074223

## Solution

#### Python
```python
a, b = map(int, input().split(" "))
if a <= b:
    diff = a
    b -= a
    print(diff, b//2)
else:
    diff = b
    a -= b
    print(diff, a//2)
 ```