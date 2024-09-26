
# Police Reqruits

Date: 26-09-2024

## Solution
#### Python
```python
length = int(input())
arr = input().split(" ")
p = 0
u = 0
for i in arr:
    if i == "-1":
        if p == 0:
            u += 1
        else:
            p -= 1
    else:
        p += int(i)
print(u)
```
        