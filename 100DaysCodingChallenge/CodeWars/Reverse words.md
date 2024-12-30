# Reverse words

Date: 07-08-2024

## Solution
#### Python
```python
def reverse_words(text):
    text = text.split(" ")
    for i in range(0, len(text)):
        text[i] = text[i][::-1]
    return " ".join(text)
```