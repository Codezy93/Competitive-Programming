# Floor Number

Date: 2024-10-26 18:21:47.060623

## Solution

#### Python
```python
for _ in range(int(input())):
    n, x = map(int, input().split())
    c = 2
    ans = 1
    while c < n:
        c += x
        ans += 1
    print(ans)
 ```