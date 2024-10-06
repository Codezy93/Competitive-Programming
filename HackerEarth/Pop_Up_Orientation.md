# Pop Up Orientation

Date: 2024-10-06 19:39:58.074223

## Solution

#### Python
```python
for _ in range(0, int(input())):
    inp = input().split(' ')
    x = int(inp[0])
    y = int(inp[1])
    l = int(inp[2])
    m = int(inp[3])
    a = int(inp[4])
    b = int(inp[5])
    if (x-a)>=l and b>=m:
        print('bottom-right')
    elif a>=l and b>=m:
        print('bottom-left')
    elif (x-a)>=l and (y-b)>=m:
        print('top-right')
    else:
        print('top-left')
 ```