
# Young Physicist

Date: 20-09-2024

## Solution
#### Python
```python
x = 0
y = 0
z = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split(" "))
    x += a
    y += b
    z += c
if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')
```
        