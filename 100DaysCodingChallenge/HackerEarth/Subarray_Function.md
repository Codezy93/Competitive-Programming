# Subarray Function

Date: 2024-10-18 00:00:00

## Solution

#### Python
```python
n, l, r = map(int, input().split())
v = list(map(int, input().split()))
arr = [i + 1 for i in range(n)]
print(' '.join(map(str, arr)))
 ```