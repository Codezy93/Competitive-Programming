# Parse int from char

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
def get_age(age):
    return int(age.replace(" years old", "")) if "years" in age else int(age.replace(" year old", ""))
 ```