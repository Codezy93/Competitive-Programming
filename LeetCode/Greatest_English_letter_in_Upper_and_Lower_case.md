# Greatest English letter in Upper and Lower case

Date: 2024-10-16 17:49:38.584114

## Solution

#### Python
```python
class Solution:
    def greatestLetter(self, s: str) -> str:
        letter = ""
        for i in s:
            if i.isupper() and i.lower() in s:
                if letter < i:
                    letter = i
            elif i.islower() and i.upper() in s:
                if letter < i.upper():
                    letter = i.upper()
        return letter
 ```