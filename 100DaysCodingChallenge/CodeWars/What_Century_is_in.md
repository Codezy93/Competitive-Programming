
# What Century is in

Date: 17-08-2024

## Solution
#### Python
```python
def what_century(year):
    year = int(year)
    if year == 1000:
        return "10th"
    century = (year - 1) // 100 + 1
    if 11 <= century <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(century % 10, "th")
    return f"{century}{suffix}"
```
        