# Is it a Palindrome

Date: 2024-11-07 00:00:00

## Solution

#### Python
```python
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
 ```