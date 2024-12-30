# Dual Issues

Date: 2024-11-12 22:19:35.073070

## Solution

#### Python
```python
def checkIfPrime(p):
    if p == 1:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True
def calculate():
    n = int(input())
    arr = list(map(int, input().split()))
    v = []
    s = set()
    for num in arr:
        if num not in s:
            s.add(num)
            if checkIfPrime(num):
                v.append(num)
    if len(v) == 0:
        return -1
    val = max(v)
    return val * val
t = int(input())
for _ in range(t):
    print(calculate())
 ```