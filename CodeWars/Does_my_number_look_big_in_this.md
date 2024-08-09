
# Does my number look big in this

Date: 09-08-2024

## Solution
#### Python
```python
def narcissistic( value ):
    value = str(value)
    sum = 0
    power = len(value)
    for i in value:
        sum += int(i)**power
    if str(sum) == value:
        return True
    else:
        return False
```
        