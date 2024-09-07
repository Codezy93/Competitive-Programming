
# Fitting Circles

Date: 07-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    L, B = map(int, input().split(" "))
    if L < B:
        temp = L
        L = B
        B = temp
    print(L//B)
```
        