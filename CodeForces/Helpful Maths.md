# Helpful Maths

Date: 06/08/2024

## Solution
#### Python
```python
a = [int(x) for x in input().split("+")]
a.sort()
a = '+'.join(map(str, a))
print(a)
```