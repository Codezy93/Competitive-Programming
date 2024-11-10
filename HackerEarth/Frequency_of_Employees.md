# Frequency of Employees

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
map = {}
for _ in range(0, int(input())):
    name = input()
    if name in map:
        map[name] += 1
    else:
        map[name] = 1
keys = list(map.keys())
keys.sort()
for i in keys:
    print(f"{i} {map[i]}")
 ```