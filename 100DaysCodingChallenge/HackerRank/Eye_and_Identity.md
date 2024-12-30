# Eye and Identity

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
import numpy as np
np.set_printoptions(legacy='1.13')
N, M = map(int, input().split(" "))
if N==M:
    print(np.identity(N))
else:
    print(np.eye(N, M, k = 0))
 ```