# Football

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
map = {}
for i in range(int(input())):
    team = input()
    if team in map:
        map[team] += 1
    else:
        map[team] = 1
max = 0
max_team = ""
for i in map:
    if map[i] > max:
        max = map[i]
        max_team = i
print(max_team)
 ```