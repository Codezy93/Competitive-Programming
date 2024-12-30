# Kefa and First Steps

Date: 2024-10-14 10:16:05.314276

## Solution

#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
max = 0
temp = 1
for i in range(len(arr)-1):
    if arr[i+1] >= arr[i]:
        temp += 1
    else:
        if temp > max:
            max = temp
        temp = 1
if temp > max:
    max = temp
print(max)
 ```