
# Total Cost

Date: 19-09-2024

## Solution
#### Python
```python
P,S,T,H,x = list(map(int,input().split()))
Sum = 0
for i in range(x):
    if S <= T:
        Sum = Sum + H
        S = S - 1
    else: 
        Sum = Sum + P
        S = S-1
print(Sum)
```
        