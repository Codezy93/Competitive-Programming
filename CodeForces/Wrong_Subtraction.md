
# Wrong Subtraction

Date: 10-08-2024

## Solution
#### Python
```python
num, k = [int(x) for x in input().split(" ")]
for _ in range(k):
    if num % 10 == 0:
        num = int(num / 10)
    else:
        num -= 1
print(num)
```
        