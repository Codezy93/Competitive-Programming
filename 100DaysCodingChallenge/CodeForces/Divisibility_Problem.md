
# Divisibility Problem

Date: 22-09-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    a,b = map(int, input().split(" "))
    if a%b == 0:
        print(0)
    else:
        print(b - (a%b))
```
        