
# Max Game

Date: 20-08-2024

## Solution
#### Python
```python
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2
    return True

for _ in range(int(input())):
    N = int(input())
    if N%2 != 0:
        N -= 1
    while isPowerOfTwo(N) == False:
        N -= 2
    print(N)
```
        