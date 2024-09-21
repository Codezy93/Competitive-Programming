
# Maximum number of words you can type

Date: 21-09-2024

## Solution
#### Python
```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        count = len(text)
        for i in text:
            for j in brokenLetters:
                if j in i:
                    count -= 1
                    break
        return (count)
```
        