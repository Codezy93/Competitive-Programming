# Day of Programmer

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    elif year % 400 == 0:
        return f"12.09.{year}"
    elif year <= 1917 and year % 4 == 0:
        return f"12.09.{year}"
    elif year % 4 == 0 and year % 100 != 0:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"
 ```