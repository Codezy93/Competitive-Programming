# Repeated Strings

Date: 2024-10-20 00:00:00

## Solution

#### Python
```python
def repeatedString(s, n):
    return (s.count('a') * (n // len(s))) + s[:n % len(s)].count('a')
 ```