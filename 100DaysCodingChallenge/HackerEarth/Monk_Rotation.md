
# Monk Rotation

Date: 22-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    x, y = map(int, input().split())
    arr = input().split(" ")
    y = y%x
    print(" ".join(arr[x-y:] + arr[0:x-y]))
```
        