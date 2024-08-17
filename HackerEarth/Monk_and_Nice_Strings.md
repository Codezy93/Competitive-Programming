
# Monk and Nice Strings

Date: 17-08-2024

## Solution
#### Python
```python
l = []
for _ in range(0, int(input())):
    a = input()
    count = 0
    for i in l:
        if a > i:
            count += 1
    l.append(a)
    print(count)
```
        