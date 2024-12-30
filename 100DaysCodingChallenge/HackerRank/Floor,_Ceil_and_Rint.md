# Floor, Ceil and Rint

Date: 2024-11-07 00:00:00

## Solution

#### Python
```python
import numpy
numpy.set_printoptions(legacy='1.13')
arr = numpy.array([float(x) for x in input().split(" ")])
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
 ```