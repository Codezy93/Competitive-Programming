
# Parity-Binary Sort

Date: 30-08-2024

## Solution
#### Python
```python
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
def parity_sort(arr):
    arr.sort(key=lambda x: (count_set_bits(x) % 2, x))
    return arr
def solve(N, a):
    arr = parity_sort(a)
    return (" ".join(map(str, arr)))
for _ in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    sorted_array = solve(N, a)
    print(sorted_array)
```
        