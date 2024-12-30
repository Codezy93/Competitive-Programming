
# Not Very Secure

Date: 16-08-2024

## Solution
#### Python
```python
import string
def alphanumeric(password):
    allowed = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if len(password) < 1:
        return False
    elif " " in password or "_" in password:
        return False
    else:
        for i in password:
            if i not in allowed:
                return False
        else:
            return True
```
        