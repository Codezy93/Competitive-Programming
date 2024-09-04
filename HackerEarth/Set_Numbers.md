
# Set Numbers

Date: 04-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    num = bin(int(input())).replace("0b", "")
    if num.count("0") == 0:
        print(int("1"*(len(num)), 2))
    elif num == "0":
        print(0)
    else:
        print(int("1"*(len(num)-1), 2))
```
        