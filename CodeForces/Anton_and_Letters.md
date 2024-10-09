# Anton and Letters

Date: 2024-10-09 17:57:48.744318

## Solution

#### Python
```python
arr = input()
if arr == "{}":
    print(0)
else:
    arr = arr.replace("{", "").replace("}", "").split(", ")
    print(len(set(arr)))
 ```