
# Nearly Lucky Number

Date: 08-08-2024

## Solution
#### Python
```python
number = input()
sevens = number.count("7")
fours = number.count("4")
digits = str(sevens + fours)
digits = digits.replace("7", "")
digits = digits.replace("4", "")
if len(digits) == 0:
    print('YES')
else:
    print('NO')
```