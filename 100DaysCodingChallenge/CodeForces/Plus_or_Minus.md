
# Plus or Minus

Date: 25-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    a, b, c = map(int, input().split())
    if a+b == c:
        print("+")
    else:
        print("-")
```
        