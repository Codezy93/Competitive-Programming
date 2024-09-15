
# Dot and Cross

Date: 15-09-2024

## Solution
#### Python
```python
import numpy
l = int(input())
A = []
B = []
for i in range(l):
    A.append([int(x) for x in input().split()])
for i in range(l):
    B.append([int(x) for x in input().split()])
print(numpy.dot(A, B))
```
        