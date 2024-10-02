
# Transportation on Vacation

Date: 02-10-2024

## Solution
#### Python
```python
def rental_car_cost(d):
    total = 40*d
    if d >= 7:
        return total-50
    elif d >= 3:
        return total-20
    else:
        return total
```
        