
# Hit The Lottery

Date: 26-08-2024

## Solution
#### Python
```python
money = int(input())
denoms = [100, 20, 10, 5, 1]
bills = 0
for i in denoms:
    bills += money//i
    money = money%i
print(bills)
```
        