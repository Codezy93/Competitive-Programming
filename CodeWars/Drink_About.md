# Drink About

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
 ```