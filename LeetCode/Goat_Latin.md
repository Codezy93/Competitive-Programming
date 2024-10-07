# Goat Latin

Date: 2024-10-07 21:37:19.085381

## Solution

#### Python
```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(" ")
        for i, j in enumerate(sentence):
            temp = 'a'*(i+1)
            if j[0] in 'aeiouAEIOU':
                sentence[i] = j + 'ma' + temp
            else:
                sentence[i] = j[1:] + j[0] + 'ma' + temp
        return " ".join(sentence)
 ```