
# Convert number to reversed array of digits

Date: 12-09-2024

## Solution
#### Python
```python
def digitize(n):
    return [int(x) for x in str(n)][::-1]
```
        