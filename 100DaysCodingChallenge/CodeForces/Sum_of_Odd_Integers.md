# Sum of Odd Integers

Date: 2024-10-19 00:00:00

## Solution

#### Python
```python
for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    if k**2 > n:
        print('NO')
    elif ((n%2==1 and k%2==1) or (n%2==0 and k%2==0)):
        print('YES')
    else:
        print('NO')
 ```