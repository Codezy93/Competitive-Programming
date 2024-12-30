# Multiple Occourance

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
for _ in range(0, int(input())):
    x = int(input())
    arr = [int(i) for i in input().split()]
    map = {}
    for j,i in enumerate(arr):
        if i in map:
            map[i].append(j+1)
        else:
            map[i] = [j+1]
    sum = 0
    for i in map:
        if len(map[i]) == 1:
            pass
        else:
            sum += map[i][-1]-map[i][0]
    print(sum)
 ```