
# Sahils Computer Address

Date: 20-09-2024

## Solution
#### Python
```python
add = input().split(".")
if len(add) != 4:
    print("NO")
else:
    for i in add:
        if not i.isdigit():
            print('NO')
            break
        elif int(i) > 255 or int(i) < 0:
            print('NO')
            break
        else:
            pass
    else:
        print('YES')
```
        