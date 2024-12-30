
# Sagars Gift

Date: 05-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    length = int(input())
    arr = input().replace(" ", "")
    arr = [int(x) for x in arr]
    arr.sort(reverse=True)
    arr = [str(x) for x in arr]
    print("".join(arr))
```
        