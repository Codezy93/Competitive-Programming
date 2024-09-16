
# Map and Lambda Functions

Date: 16-09-2024

## Solution
#### Python
```python
cube = lambda x: x**3

def fibonacci(n):
    fib = [0, 1]
    if n == 1:
        return [0]
    if n == 0:
        return []
    for i in range(n-2):
        fib.append(fib[-2]+fib[-1])
    return fib
```
        