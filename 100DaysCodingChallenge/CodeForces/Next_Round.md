
# Next Round

Date: 01-09-2024

## Solution
#### Python
```python
N, K = map(int, input().split(" "))
arr = [int(x) for x in input().split(" ")]
count = 0
for i in arr:
    if i >= arr[K-1] and i > 0:
        count += 1
print(count)
```
        