# Sum the String

Date: 2024-10-09 17:57:48.744318

## Solution

#### Python
```python
def sum_str(a, b):
    if a == "":
        a = 0
    else:
        a = int(a)
    if b == "":
        b = 0
    else:
        b = int(b)
    return str(int(a) + int(b))
 ```