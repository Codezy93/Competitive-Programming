# Anagram Detection

Date: 2024-10-31 00:00:00

## Solution

#### Python
```python
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    map1 = {}
    map2 = {}
    for i in test:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1
    for i in original:
        if i in map2:
            map2[i] += 1
        else:
            map2[i] = 1
    return map1 == map2
 ```