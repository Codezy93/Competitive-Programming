# Clock Conversion

Date: 2024-11-12 22:19:35.073070

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    s = input()
    h = int(s[:2])
    if h == 0:
        print("12" + s[2:5], "AM")
    elif h == 12:
        print(s, "PM")
    elif h > 12:
        nh = h - 12
        print(f"{nh:02d}:{s[3:5]}", "PM")
    else:
        print(s, "AM")
 ```