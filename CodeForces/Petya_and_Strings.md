
# Petya and Strings

Date: 08-09-2024

## Solution
#### Python
```python
s1 = input().lower()
s2 = input().lower()
for x, y in enumerate(s1):
    if s1[x] > s2[x]:
        print(1)
        break
    elif s2[x] > s1[x]:
        print(-1)
        break
    else:
        pass
else:
    print(0)
```
        