# Fake Binary

Date: 2024-10-21 00:00:00

## Solution

#### Python
```python
def fake_bin(string):
    return "".join(["1" if int(x)>=5 else "0" for x in string])
 ```