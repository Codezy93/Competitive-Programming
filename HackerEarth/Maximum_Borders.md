
# Maximum Borders

Date: 25-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    n, m = map(int, input().split())
    matrix = []
    max_black = 0
    for i in range(0, n):
        a = input()
        temp = a.split('.')
        temp = [len(x) for x in temp]
        if max(temp) > max_black:
            max_black = max(temp)
        matrix.append(a)
    for i in range(0, m):
        count = 0
        temp = ""
        for j in range(0, n):
            temp = temp + matrix[j][i]
        temp = temp.split('.')
        temp = [len(x) for x in temp]
        if max(temp) > max_black:
            max_black = max(temp)
    print(max_black)
```
        