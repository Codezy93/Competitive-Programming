
# Find the Odd Int

Date: 04-09-2024

## Solution
#### Python
```python
def find_it(seq):
    map = {}
    for i in seq:
        if(i in map):
            map[i] += 1
        else:
            map[i] = 1
    for i in map:
        if (map[i]%2!=0):
            return i
```
        