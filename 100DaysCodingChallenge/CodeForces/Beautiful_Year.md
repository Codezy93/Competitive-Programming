
# Beautiful Year

Date: 09-08-2024

## Solution
#### Python
```python
year = int(input())
while True:
    year += 1
    oper = set(list(str(year)))
    if len(oper) == 4:
        print(year)
        break
```
        