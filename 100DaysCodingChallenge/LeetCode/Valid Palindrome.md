# Valid Palindrome

Date: 05/08/2024

## Solution
#### Python
```python
import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = string.ascii_lowercase + string.digits
        s = s.lower()
        s = s.replace(" ", "")
        word = ""
        for i in s:
            if i in allowed:
                word += i
        if word == word[::-1]:
            return True
        else:
            return False
```