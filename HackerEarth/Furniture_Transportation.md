
# Furniture Transportation

Date: 16-09-2024

## Solution
#### Python
```python
N, I, M = map(int, input().split(" "))
arr = [int(x) for x in input().split(" ")]
count = 0
for i in range(0, N-M+1):
    for j in arr[i:i+M]:
        if j > I:
            break
    else:
        count += 1
print(count)
```
        