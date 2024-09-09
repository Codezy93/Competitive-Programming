
# Jaden Casing String

Date: 09-09-2024

## Solution
#### Python
```python
def to_jaden_case(string):
    string = string.split(" ")
    for x, y in enumerate(string):
        string[x] = y.capitalize()
    return " ".join(string)
```
        