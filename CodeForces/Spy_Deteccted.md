
# Spy Deteccted

Date: 27-09-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    l = int(input())
    arr = input().split(" ")
    for i in set(arr):
        if arr.count(i) == 1:
            print(arr.index(i)+1)
```
        