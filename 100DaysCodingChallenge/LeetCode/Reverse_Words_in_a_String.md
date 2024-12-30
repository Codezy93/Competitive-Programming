# Reverse Words in a String

Date: 2024-10-27 00:00:00

## Solution

#### Python
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = []
        temp = ""
        for i in s:
            if i != " ":
                temp += i
            else:
                if temp != "":
                    sentence.insert(0, temp)
                    temp = ""
        if temp != "":
            sentence.insert(0, temp)
        return " ".join(sentence)
 ```