
# Sum

Date: 13-09-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    a, b, c = map(int, input().split(' '))
    if a+b==c:
        print('YES')
    elif b+c==a:
        print('YES')
    elif c+a==b: 
        print('YES')
    else:
        print('NO')
```
        