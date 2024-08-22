
# Replace with Alphabet Position

Date: 22-08-2024

## Solution
#### Python
```python
def alphabet_position(text):
    string = list("abcdefghijklmnopqrstuvwxyz")
    encode = []
    text = text.lower()
    for i in text:
        if i in string:
            encode.append(str(string.index(i)+1))
    return " ".join(encode)
```
        