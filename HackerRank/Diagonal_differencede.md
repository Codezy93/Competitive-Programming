
# Diagonal differencede

Date: 30-09-2024

## Solution
#### Python
```python
diagonalDifference(arr):
    a, b = 0, 0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][len(arr)-1-i]
    return (abs(a-b))
```
        