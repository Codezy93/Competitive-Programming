# Gemstones

Date: 2024-10-17 00:00:00

## Solution

#### Python
```python
def gemstones(arr):
    gem = set(list(arr[0]))
    del arr[0]
    for i in arr:
        gem = gem.intersection(set(list(i)))
    return len(gem)
 ```