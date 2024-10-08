# Correct the mistakes of the character recognition software

Date: 2024-10-08 09:11:16.441053

## Solution

#### Python
```python
def correct(s):
    s = s.replace('5', 'S').replace("0", 'O').replace('1', 'I')
    return s
 ```