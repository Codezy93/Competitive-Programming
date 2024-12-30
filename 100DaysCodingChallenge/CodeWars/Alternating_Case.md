# Alternating Case

Date: 2024-10-07 21:37:19.085381

## Solution

#### Python
```python
def to_alternating_case(string):
    string = list(string)
    for i, j in enumerate(string):
        if j.isupper():
            string[i] = j.lower()
        else:
            string[i] = j.upper()
    return "".join(string)
 ```