# Choosing Teams

Date: 2024-11-02 00:00:00

## Solution

#### Python
```python
n, k = map(int, input().split())
count = 0
arr = [int(x) for x in input().split()]
for i in arr:
    if i <= (5 - k):
        count += 1
team = count // 3
print(team)
 ```