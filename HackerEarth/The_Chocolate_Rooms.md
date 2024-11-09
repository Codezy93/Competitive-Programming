# The Chocolate Rooms

Date: 2024-11-09 19:13:28.406394

## Solution

#### Python
```python
def solve(N, K, chocolates):
    arr = []
    for i in chocolates:
        i = i[1:]
        arr = arr + i
    return "Yes" if len(set(arr)) >= K else "No"
T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split(' ')))
    chocolates = []
    for _ in range(N):
        chocolates.append(input().split(' '))
    out_ = solve(N, K, chocolates)
    print (out_)
 ```