
# Create Phone Number

Date: 08-08-2024

## Solution
#### Python
```python
def create_phone_number(n):
    n = [str(x) for x in n]
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, " ")
    n.insert(9, "-")
    return (str("".join(n)))
```