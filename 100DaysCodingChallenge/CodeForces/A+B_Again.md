
# A+B Again

Date: 20-08-2024

## Solution
#### Python
```python
for i in range(int(input())):
    num = int(input())
    a, b = ((num-num%10)/10, num%10)
    print(int(a+b))
```
        