# Century from year

Date: 2024-10-22 00:00:00

## Solution

#### Python
```python
def century(year):
    return year // 100 if year % 100 == 0 else year // 100 + 1
 ```