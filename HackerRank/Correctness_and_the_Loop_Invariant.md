# Correctness and the Loop Invariant

Date: 2024-10-23 00:00:00

## Solution

#### Python
```python
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
ar.sort()
print(" ".join(map(str,ar)))
 ```