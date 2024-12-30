
# Split Houses

Date: 19-08-2024

## Solution
#### Python
```python
length = int(input())
arr = input()
if "HH" in arr:
    print('NO')
else:
    arr = arr.replace(".", "B")
    print('YES')
    print(arr)
```
        