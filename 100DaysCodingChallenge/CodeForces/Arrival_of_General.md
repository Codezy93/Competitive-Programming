# Arrival of General

Date: 2024-10-13 19:26:26.421996

## Solution

#### Python
```python
length = int(input())
arr = list(map(int, input().split(" ")))
steps = 0
max_val = arr.index(max(arr))
steps += max_val
temp = max(arr)
del arr[max_val]
arr.insert(0, temp)
arr.reverse()
min_val = arr.index(min(arr))
steps += min_val
print(steps)
 ```