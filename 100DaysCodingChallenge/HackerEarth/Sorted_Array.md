# Sorted Array

Date: 2024-10-05 00:00:00

## Solution

#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
steps = 0
for i in range(0, len(arr)-1):
    if i == 0:
        pass
    elif arr[i] >= arr[i+1]:
        steps += arr[i] - arr[i+1] + 1
        arr[i+1] = arr[i] + 1
    else:
        pass
print(steps)
 ```