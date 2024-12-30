
# Magnets

Date: 15-08-2024

## Solution
#### Python
```python
last = ""
groups = 0
for i in range(0, int(input())):
    a = input()
    if a != last:
        groups += 1
        last = a
print(groups)
```
        