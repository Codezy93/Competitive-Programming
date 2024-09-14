
# Total Amount of Points

Date: 14-09-2024

## Solution
#### Python
```python
def points(games):
    x = 0
    for i in games:
        a,b = map(int, i.split(":"))
        if a > b:
            x += 3
        elif a == b:
            x += 1
        else:
            pass
    return x
```
        