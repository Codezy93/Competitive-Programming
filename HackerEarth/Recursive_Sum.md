# Recursive Sum

Date: 2024-10-07 21:37:19.085381

## Solution

#### Python
```python
for _ in range(int(input())):
    temp = 0
    for i in range(int(input())):
        a, b = map(int, input().split(" "))
        temp += a*b
    while temp > 9:
        temp = sum(map(int, list(str(temp))))
    print(temp)
 ```