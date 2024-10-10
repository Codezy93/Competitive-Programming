# Vowel Count

Date: 2024-10-10 18:29:44.688592

## Solution

#### Python
```python
def get_count(sentence):
    length = len(sentence)
    for i in "aeiouAEIOU":
        sentence = sentence.replace(i, "")
    return length - len(sentence)
 ```