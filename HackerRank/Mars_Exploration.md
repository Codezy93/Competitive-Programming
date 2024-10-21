# Mars Exploration

Date: 2024-10-21 00:00:00

## Solution

#### Python
```python
def marsExploration(s):
    ideal = "SOS" * (len(s)//3)
    count = 0
    for i, j in zip(s, ideal):
        if i != j:
            count += 1
    return count
 ```