# Polynomials

Date: 2024-11-11 19:31:48.048247

## Solution

#### Python
```python
import numpy as np
arr = [float(x) for x in input().split(" ")]
P = float(input())
print(np.polyval(arr, P))
 ```