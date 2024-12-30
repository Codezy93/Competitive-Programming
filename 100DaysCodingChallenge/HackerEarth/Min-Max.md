
# Min-Max

Date: 15-09-2024

## Solution
#### Python
```python
l = int(input())
arr = [int(x) for x in input().split()]
for i in range(min(arr), max(arr)):
    if i not in arr:
        print('NO')
        break
else:
    print('YES')
```
        