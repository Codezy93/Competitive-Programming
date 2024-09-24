
# MinMaxSum

Date: 24-09-2024

## Solution
#### Python
```python
def miniMaxSum(arr):
    total = sum(arr)
    min_total = total-max(arr)
    max_total = total-min(arr)
    print(min_total, max_total)
```
        