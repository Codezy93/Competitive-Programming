# Halloween Sale

Date: 2024-10-13 19:26:26.421996

## Solution

#### Python
```python
price = result = last_price = 0
    while price <= s:
        if result == 0:
            last_price = p
        elif last_price - d > m:
            last_price = last_price - d
        else:
            last_price = m
        price += last_price
        result += 1
    return result - 1
 ```