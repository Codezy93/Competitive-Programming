
# Vanya and Fence

Date: 06-09-2024

## Solution
#### Python
```python
N, H = map(int, input().split(" "))
arr = [int(x) for x in input().split(" ")]
arr = [2 if x > H else 1 for x in arr]
print(sum(arr))
```
        