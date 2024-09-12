
# Symmetric Difference

Date: 12-09-2024

## Solution
#### Python
```python
l1 = input()
a1 = [int(x) for x in input().split(" ")]
l2 = input()
a2 = [int(x) for x in input().split(" ")]
res = []
for i in set(a2).difference(set(a1)):
    res.append(i)
for i in set(a1).difference(set(a2)):
    res.append(i)
res.sort()
for i in res:
    print(i)
```
        