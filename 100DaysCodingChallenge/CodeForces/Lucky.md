
# Lucky

Date: 21-08-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    number = input()
    num1 = sum([int(x) for x in number[0:3]])
    num2 = sum([int(x) for x in number[3:]])
    if num1 == num2:
        print("YES")
    else:
        print("NO")
```
        