# Divisibility

Date: 07-08-2024

## Solution
#### Python
```python
N = int(input())
data = [x for x in input().split()]
if data[-1][-1] == "0":
    print('Yes')
else:
    print("No")
```