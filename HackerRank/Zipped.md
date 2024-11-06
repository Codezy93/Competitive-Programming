# Zipped

Date: 2024-11-06 00:00:00

## Solution

#### Python
```python
m, n = map(int, input().split(" "))
matrix = []
for _ in range(n):
    matrix.append([float(x) for x in input().split(" ")])
for i in zip(*matrix):
    print(sum(i)/n)
 ```