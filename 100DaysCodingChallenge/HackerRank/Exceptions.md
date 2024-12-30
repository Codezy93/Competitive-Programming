
# Exceptions

Date: 24-08-2024

## Solution
#### Python
```python
digits = "123456789"
for _ in range(int(input())):
    n, d = [x for x in input().split(" ")]
    if d == "0":
        print("Error Code: integer division or modulo by zero")
    elif d not in digits:
        print(f"Error Code: invalid literal for int() with base 10: '{d}'")
    elif n not in digits and n != "0":
        print(f"Error Code: invalid literal for int() with base 10: '{n}'")
    else:
        print(int(n)//int(d))
```
        