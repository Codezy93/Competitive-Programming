# Multiply by 2 divide by 6

Date: 2024-11-07 00:00:00

## Solution

#### Python
```python
for _ in range(int(input())):
    n = int(input())
    moves = 0
    possible = True
    while n > 1:
        if n % 6 == 0:
            n //= 6
            moves += 1
        elif n % 3 == 0:
            n *= 2
            moves += 1
        else:
            possible = False
            break
    if possible and n == 1:
        print(moves)
    else:
        print(-1)
 ```