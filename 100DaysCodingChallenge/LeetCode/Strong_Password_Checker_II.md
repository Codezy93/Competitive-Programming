# Strong Password Checker II

Date: 2024-11-12 22:19:35.073070

## Solution

#### Python
```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        lower = 0
        upper = 0
        digit = 0
        spchar = 0
        for i in range(0, len(password)-1):
            if password[i].islower():
                lower += 1
            elif password[i].isupper():
                upper += 1
            elif password[i].isdigit():
                digit += 1
            elif password[i] in "!@#$%^&*()-+":
                spchar += 1
            else:
                pass
            if password[i] == password[i+1]:
                return False
        if password[-1].islower():
            lower += 1
        elif password[-1].isupper():
            upper += 1
        elif password[-1].isdigit():
            digit += 1
        elif password[-1] in "!@#$%^&*()-+":
            spchar += 1
        else:
            pass
        if lower > 0 and upper > 0 and digit > 0 and spchar > 0 and len(password) >= 8:
            return True
        else:
            return False
 ```