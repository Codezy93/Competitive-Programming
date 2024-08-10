
# Set.Add()

Date: 10-08-2024

## Solution
#### Python
```python
elems = []
for _ in range(int(input())):
    inp = input()
    if inp in elems:
        pass
    else:
        elems.append(inp)
print(len(elems))
```
        