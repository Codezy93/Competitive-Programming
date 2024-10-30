# Cats and Mouse

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
def catAndMouse(x, y, z):
    a = abs(z-x)
    b = abs(z-y)
    if a>b:
        return "Cat B"
    elif b>a:
        return "Cat A"
    else:
        return "Mouse C"
 ```