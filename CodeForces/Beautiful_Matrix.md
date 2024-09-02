
# Beautiful Matrix

Date: 02-09-2024

## Solution
#### Python
```python
matrix = []
for i in range(5):
    matrix.append(input())
matrix = [[int(y) for y in x.split(" ")] for x in matrix]
for i, j in enumerate(matrix):
    if 1 in j:
        print(abs(i+1-3)+abs(j.index(1)+1-3))
        break
```
        