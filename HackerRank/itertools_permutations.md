
# itertools permutations

Date: 05-09-2024

## Solution
#### Python
```python
from itertools import permutations
S, K = input().split(" ")
K = int(K)
for perm in sorted(permutations(S, K)):
    print("".join(perm))
```
        