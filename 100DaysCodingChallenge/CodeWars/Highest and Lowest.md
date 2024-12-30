# Highest and Lowest

Date: 05/08/2024

## Solution
#### Python
```python
def high_and_low(numbers):
    numbers = numbers.split(" ")
    list_num = [int(x) for x in numbers]
    return f"{max(list_num)} {min(list_num)}"
```