# CamelCase

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
def camelcase(s):
    steps = 1
    for i in s:
        if i.isupper():
            steps += 1
    return steps
 ```