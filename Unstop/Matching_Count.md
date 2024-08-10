
# Matching Count

Date: 10-08-2024

## Solution
#### Python
```python
typed = []
color = []
name = []
for _ in range(0, int(input())):
  inp = input().split(" ")
  typed.append(inp[0])
  color.append(inp[1])
  name.append(inp[2])
search = input()
if search == "type":
  print(typed.count(input()))
if search == "color":
  print(color.count(input()))
if search == "name":
  print(name.count(input()))
```
        