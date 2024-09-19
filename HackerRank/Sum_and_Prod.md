
# Sum and Prod

Date: 19-09-2024

## Solution
#### Python
```python
import numpy
N, M = map(int, input().split(" "))
matrix = []
for i in range(N):
    matrix.append([int(x) for x in input().split(" ")])
matrix = numpy.array(matrix)
print(numpy.prod(numpy.sum(matrix, axis=0)))
```
        