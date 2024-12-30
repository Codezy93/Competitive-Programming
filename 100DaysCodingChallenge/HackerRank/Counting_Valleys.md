# Counting Valleys

Date: 2024-10-19 00:00:00

## Solution

#### Python
```python
def countingValleys(steps, path):
    valleys = 0
    level = 0
    for step in path:
        level += 1 if step == "U" else -1
        if level == 0 and step == "U":
            valleys += 1
    return valleys
 ```