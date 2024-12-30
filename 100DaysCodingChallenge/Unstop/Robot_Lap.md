
# Robot Lap

Date: 09-08-2024

## Solution
#### Python
```python
dirs = input()
if " " in dirs:
  dirs = dirs.split(" ")[1]
else:
  dirs = input()

if dirs.count("U") == dirs.count("D"):
  if dirs.count("L") == dirs.count("R"):
    print("YES")
  else:
    print("NO")
else:
  print("NO")
```
        