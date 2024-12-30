# Little Jhool and the Magical Jewels

Date: 2024-10-23 00:00:00

## Solution

#### Python
```python
for _ in range(0, int(input())):
    map = {}
    string = input()
    for i in string:
        if i in ["r","u","b","y"]:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
    min = 999999
    if len(map.keys()) == 4:
        for i in map:
            if map[i] < min:
                min = map[i]
        print(min)
    else:
        print(0)
 ```