
# Registration System

Date: 28-08-2024

## Solution
#### Python
```python
map = {}
for i in range(int(input())):
    name = input()
    if name not in map:
        map[name] = 1
        print("OK")
    else:
        print(f"{name}{map[name]}")
        map[name] += 1
```
        