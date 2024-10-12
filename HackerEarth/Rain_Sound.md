# Rain Sound

Date: 2024-10-12 18:03:23.457274

## Solution

#### Python
```python
for _ in range(int(input())):
    l,r,s = map(int,input().split())
    if s > r:
        print(-1,-1)
    else:
        mi = int(((l-1)/s) + 1)
        ma = r//s
        if mi>ma:
            print(-1,-1)
        else:
            print(mi,ma)
 ```