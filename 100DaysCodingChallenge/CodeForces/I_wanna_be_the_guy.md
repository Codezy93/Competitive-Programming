# I wanna be the guy

Date: 2024-10-10 18:29:44.688592

## Solution

#### Python
```python
n = int(input())
p = input().split(" ")
q = input().split(" ")
a = p[0]
b = q[0]
p = p[1:]
q = q[1:]
if len(set(p + q)) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
 ```