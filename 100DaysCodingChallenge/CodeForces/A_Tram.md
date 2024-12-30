
# A Tram

Date: 12-08-2024

## Solution
#### Python
```python
seat = [0]
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    seat.append(seat[-1]-int(a)+int(b))
print(max(seat))
```
        