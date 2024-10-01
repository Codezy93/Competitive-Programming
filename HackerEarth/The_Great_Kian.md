
# The Great Kian

Date: 01-10-2024

## Solution
#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
a = 0
b = 0
c = 0
index = 0
while index<length:
    a = a + arr[index]
    try:
        b = b + arr[index+1]
    except:
        pass
    try:
        c = c + arr[index+2]
    except:
        pass
    index += 3
print(a, b, c)
```
        