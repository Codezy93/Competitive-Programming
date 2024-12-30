# Transpose and Flatten

Date: 2024-11-09 19:13:28.406394

## Solution

#### Python
```python
import numpy as np
N, M = map(int, input().split(" "))
matrix = np.array([[int(x) for x in input().split(" ")] for i in range(N)])
print(np.transpose(matrix))
print(matrix.flatten())
 ```