
# Inner and Outer

Date: 13-09-2024

## Solution
#### Python
```python
import numpy
a,b = map(int, input().split(' '))
c,d = map(int, input().split(' '))
A = numpy.array([a, b])
B = numpy.array([c, d])
print(numpy.inner(A, B))
print(numpy.outer(A, B))
```
        