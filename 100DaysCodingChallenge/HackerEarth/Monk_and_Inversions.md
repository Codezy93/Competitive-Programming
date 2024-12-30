
# Monk and Inversions

Date: 24-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    N = int(input())
    counter = 0
    matrix = []
    for i in range(N):
        matrix.append([int(x) for x in input().split(" ")])
    for i in range(N):
        for j in range(N):
            for k in range(i, N):
                for l in range(j, N):
                    if matrix[i][j] > matrix[k][l]:
                        counter += 1
    print(counter)
```
        