# Games

Date: 2024-10-21 00:00:00

## Solution

#### Python
```python
h = []
g = []
for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    h.append(a)
    g.append(b)
sum = 0
for i in h:
    sum += g.count(i)
print(sum)
 ```