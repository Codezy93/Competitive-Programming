
# Rest in Peace - 21-1

Date: 14-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    number = input()
    if "21" in number or int(number)%21 == 0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
```
        