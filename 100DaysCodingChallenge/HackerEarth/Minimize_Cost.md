
# Minimize Cost

Date: 08-09-2024

## Solution
#### Python
```python
def Solve (k, arr):
    j = 1
    res = 0
    i = 0
    while i < n:
        j = 1
        res += abs(arr[i])
        if arr[i] > 0:
            while j <= k and i + j < len(arr):
                if arr[i + j] < 0:
                    res += arr[i + j]
                else:
                    break
                j += 1
        i += j
    return(abs(res))
n, k = map(int, input().split())
arr = [int(x) for x in input().split()]
out_ = Solve(k, arr)
print (out_)
```
        