# Sales by match

Date: 2024-10-10 18:29:44.688592

## Solution

#### Python
```python
def sockMerchant(n, ar):
    map = {}
    count = 0
    for i in ar:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    for i in map:
        count += map[i]%2
    return (len(ar)-count)//2
 ```