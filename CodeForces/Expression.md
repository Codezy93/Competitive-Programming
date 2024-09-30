
# Expression

Date: 30-09-2024

## Solution
#### Python
```python
a, b, c = map(int, [input(), input(), input()])
print(max([a+b+c,
    a*b*c,
    a*b+c,
    a+b*c,
    a*(b+c),
    (a+b)*c,
    (a*b)+c,
    a+(b*c)
]))
```
        