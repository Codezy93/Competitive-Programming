# Find the median

Date: 2024-10-11 00:00:00

## Solution

#### Python
```python
def findMedian(arr):
    arr.sort()
    if len(arr)%2 == 0:
        return (arr[len(arr)//2]+arr[(len(arr)//2)+1])//2
    else:
        return arr[(len(arr)//2)]
 ```