# Presents

Date: 2024-10-05 00:00:00

## Solution

#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
for i in range(1, length+1):
    print(arr.index(i)+1, end=" ")
 ```