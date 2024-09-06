
# itertools Product

Date: 06-09-2024

## Solution
#### Python
```python
from itertools import product
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
l = list(product(*[a,b]))
for i in l:
    print(i, end=" ")
```
        