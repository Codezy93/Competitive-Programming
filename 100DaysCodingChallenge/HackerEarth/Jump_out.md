
# Jump out

Date: 23-09-2024

## Solution
#### Python
```python
l = int(input())
for i, j in enumerate([int(x) for x in input().split(" ")]):
    if i+j+1 > l:
        print(i+1)
        break
```
        