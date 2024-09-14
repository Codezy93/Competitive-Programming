
# Final Destination

Date: 14-09-2024

## Solution
#### Python
```python
x, y = 0, 0
for i in input():
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    else:
        y -= 1
print(x, y)
```
        