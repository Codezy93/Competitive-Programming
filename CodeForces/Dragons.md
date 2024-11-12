# Dragons

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
t = 1000
a = [(0, 0)] * t
while True:
    try:
        s, n = map(int, input().split())
        dragons = []
        for _ in range(n):
            x, y = map(int, input().split())
            dragons.append((x, y))
        dragons.sort()
        possible = True
        for dragon in dragons:
            if s <= dragon[0]:
                possible = False
                break
            else:
                s += dragon[1]
        if possible:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
 ```