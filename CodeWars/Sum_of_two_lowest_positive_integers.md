# Sum of two lowest positive integers

Date: 2024-10-18 00:00:00

## Solution

#### Python
```python
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])
 ```