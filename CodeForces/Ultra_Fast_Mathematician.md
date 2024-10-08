# Ultra Fast Mathematician

Date: 2024-10-08 09:11:16.441053

## Solution

#### Python
```python
a = input()
b = input()
res = ""
for i, j in zip(a, b):
    if i == j:
        if i == 0:
            res = res + "1"
        else:
            res = res + "0"
    else:
        res = res + "1"
print(res)
 ```