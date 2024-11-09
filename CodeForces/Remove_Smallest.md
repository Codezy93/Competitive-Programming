# Remove Smallest

Date: 2024-11-09 19:13:28.406394

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = n
    for i in range(n - 1):
        if arr[i] == arr[i + 1] or arr[i + 1] - arr[i] == 1:
            count -= 1
    if count != 1:
        print("NO")
    else:
        print("YES")
 ```