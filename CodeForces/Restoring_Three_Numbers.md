# Restoring Three Numbers

Date: 2024-10-24 00:00:00

## Solution

#### Python
```python
a = list(map(int,input().split()))
maks = 0
def biggest(data, maks):
    minus = []
    for i in data:
        if i >= maks:
            maks = i
        else:
            continue
    for i in data:
        if i != maks:
            minus.append(i)
        else:
            continue
    for i in minus:
        print(maks - i, end=" ")

biggest(a, maks)
 ```