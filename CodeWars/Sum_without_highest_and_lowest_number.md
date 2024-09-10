
# Sum without highest and lowest number

Date: 10-09-2024

## Solution
#### Python
```python
def sum_array(arr):
    if arr == None or len(arr) <= 2:
        return 0
    arr.sort()
    return sum(arr[1:-1])
```
        