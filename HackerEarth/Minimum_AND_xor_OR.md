
# Minimum AND xor OR

Date: 26-08-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()  # Sort the array
    min_val = float('inf')
    for i in range(len(arr) - 1):
        # Compare only adjacent elements after sorting
        temp = (arr[i] & arr[i + 1]) ^ (arr[i] | arr[i + 1])
        if temp < min_val:
            min_val = temp
    print(min_val)
```
        