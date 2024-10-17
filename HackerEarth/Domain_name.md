# Domain name

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
import re
integer_expr = re.compile(r'(?=^.{4,253}$)(^((?!-)[a-zA-Z0-9-]{0,62}[a-zA-Z0-9]\.)+[a-zA-Z]{2,63}$)')
for _ in range(int(input())):
    x = input()
    for ch in x:
        c = 0
        if (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122) or (48 <= ord(ch) <= 57) or (ch == '.') or (ch == '-'):
            c = 1
        assert c == 1
    if integer_expr.match(x):
        print("true")
    else:
        print("false")
 ```