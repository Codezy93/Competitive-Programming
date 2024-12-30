
# I_love_%username%

Date: 19-08-2024

## Solution
#### Python
```python
length = int(input())
scores = [int(x) for x in input().split()]
min_score = scores[0]
max_score = scores[0]
amazing = 0
for i, j in enumerate(scores):
    if i == 0:
        pass
    else:
        if j > max_score:
            amazing += 1
            max_score = j
        elif j < min_score:
            amazing += 1
            min_score = j
        else:
            pass
print(amazing)
```
        