
# Hulk

Date: 16-09-2024

## Solution
#### Python
```python
toggle = True
out = []
iter = int(input())
for i in range(iter):
    if i == iter-1 and toggle:
        out.append('I hate it')
    elif i == iter-1:
        out.append('I love it')
    elif toggle:
        out.append('I hate that')
    else:
        out.append('I love that')
    toggle = not toggle
print(' '.join(out))
```
        