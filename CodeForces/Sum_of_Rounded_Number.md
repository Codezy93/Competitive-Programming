
# Sum of Rounded Number

Date: 02-10-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    num = int(input())
    if num <= 10:
        print(1)
        print(num)
    else:
        out = []
        for i in range(1, len(str(num))+1):
            temp = num%(10**i)
            if temp != 0:
                out.append(str(temp))
            num -= temp
        print(len(out))
        print(" ".join(out))
```
        