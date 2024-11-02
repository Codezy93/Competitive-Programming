# Crazy Kangaroo

Date: 2024-11-02 00:00:00

## Solution

#### Python
```python
for _ in range(0, int(input())):
    a,b,m = map(int,input().split())
    ans =0 
    for i in range(a,b+1):
        if i%m == 0 :
            ans +=1
    print(ans)
 ```