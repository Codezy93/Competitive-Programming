
# Find Pairs

Date: 27-08-2024

## Solution
#### Python
```python
length = int(input())
arr = [int(x) for x in input().split()]
count = 0
diff_map = {}
for i in range(len(arr)):
    diff = arr[i] - i
    if diff in diff_map:
        count += diff_map[diff]
    if diff in diff_map:
        diff_map[diff] += 1
    else:
        diff_map[diff] = 1
print(count*2)
```
        