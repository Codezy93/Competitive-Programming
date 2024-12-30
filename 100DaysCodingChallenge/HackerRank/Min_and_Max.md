
# Min and Max

Date: 14-09-2024

## Solution
#### Python
```python
import numpy
a,b = map(int, input().split(' '))
arr = []
for _ in range(a):
    arr.append([int(x) for x in input().split(' ')])
arr = numpy.array(arr)
arr = numpy.min(arr, axis = 1)
arr = numpy.max(arr)
print(arr)
```
        