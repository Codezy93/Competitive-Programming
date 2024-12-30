# Minimum Distances

Date: 2024-10-16 17:49:38.584114

## Solution

#### Python
```python
def minimumDistances(a):
    min = float('inf')
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                if abs(i-j) < min:
                    min = abs(i-j)
    return min if min != float('inf') else -1
 ```