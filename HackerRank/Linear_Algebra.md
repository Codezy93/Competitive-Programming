
# Linear Algebra

Date: 09-09-2024

## Solution
#### Python
```python
import numpy as np
matrix = [list(map(float, input().split())) for _ in range(int(input()))]
print(round(np.linalg.det(matrix), 2))
```
        