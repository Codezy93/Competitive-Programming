# Concatenate

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
import numpy
N, M, P = map(int, input().split(" "))
print(numpy.concatenate((numpy.array([[int(x) for x in input().split(" ")]for i in range(N)]),numpy.array([[int(x) for x in input().split(" ")]for i in range(M)]))))
 ```