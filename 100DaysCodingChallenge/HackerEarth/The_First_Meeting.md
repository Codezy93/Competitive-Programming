# The First Meeting

Date: 2024-10-31 00:00:00

## Solution

#### Python
```python
def isprime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if(n%i==0):
            return False
            break
    else:
        return True
N = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
minval = 0
maxval = 0
for i in arr:
    if isprime(i):
        minval = i
        break
arr.sort(reverse=True)
for i in arr:
    if isprime(i):
        maxval = i
        break
if minval == 0 and maxval == 0:
    print(-1)
else:
    print(abs(minval-maxval))
 ```