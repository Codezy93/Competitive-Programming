
# Descending Order

Date: 18-09-2024

## Solution
#### Python
```python
def descending_order(num):
    num = [int(x) for x in list(str(num))]
    num.sort(reverse=True)
    num = [str(x) for x in num]
    return int("".join(num))
```
        