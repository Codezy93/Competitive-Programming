# Lexological Rows

Date: 2024-10-19 00:00:00

## Solution

#### Python
```python
n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
del_col = [0] * m
ans = 0
for j in range(m):
    need_to_delete = False
    for i in range(1, n):
        if a[i][j] < a[i - 1][j]:
            can_fix = False
            for k in range(j):
                if del_col[k] == 0 and a[i][k] > a[i - 1][k]:
                    can_fix = True
                    break
            if not can_fix:
                need_to_delete = True
                break
    del_col[j] = 1 if need_to_delete else 0
    ans += del_col[j]
print(ans)
 ```