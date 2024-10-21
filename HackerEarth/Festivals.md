# Festivals

Date: 2024-10-21 00:00:00

## Solution

#### Python
```python
for _ in range(int(input())):
    map = {}
    for i in range(int(input())):
        key, freq = input().split(" ")
        if key in map:
            map[key].append(int(freq))
        else:
            map[key] = [int(freq)]
    max = 0
    max_key = ""
    for i in map:
        if len(map[i]) > 3:
            map[i].sort()
            map[i] = sum(map[i][-3:])
        else:
            map[i] = sum(map[i])
        if map[i] > max:
            max = map[i]
            max_key = i
        elif map[i] == max and max_key > i:
            max = map[i]
            max_key = i
        else:
            pass
    print(max_key, max)
 ```