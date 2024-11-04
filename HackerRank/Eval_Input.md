# Eval Input

Date: 2024-11-04 00:00:00

## Solution

#### Python
```python
x, y = map(int, input().split(" "))
query = input().replace('x', str(x))
print(eval(query)==y)
 ```