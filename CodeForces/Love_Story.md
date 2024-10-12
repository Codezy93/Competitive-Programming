# Love Story

Date: 2024-10-12 18:03:23.457274

## Solution

#### Python
```python
for _ in range(int(input())):
    print(sum([int(x!=y) for x, y in zip('codeforces', input())]))
 ```