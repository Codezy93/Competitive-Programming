# Angry Professors

Date: 2024-10-31 00:00:00

## Solution

#### Python
```python
def angryProfessor(k, a):
    steps = 0
    for i in a:
        if i <= 0:
            steps += 1
    if steps >= k:
        return "NO"
    else:
        return "YES"
 ```