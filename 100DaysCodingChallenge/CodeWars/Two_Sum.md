
# Two Sum

Date: 27-09-2024

## Solution
#### Python
```python
def two_sum(numbers, target):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == target:
                return (i, j)
    return -1
```
        