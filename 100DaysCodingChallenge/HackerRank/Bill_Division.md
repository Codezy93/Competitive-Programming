
# Bill Division

Date: 26-09-2024

## Solution
#### Python
```python
def bonAppetit(bill, k, b):
    total = int(round((sum(bill)-bill[k])/2, 0))
    if total == b:
        print("Bon Appetit")
    else:
        print(b-total)
```
        