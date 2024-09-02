
# Case Conversion

Date: 02-09-2024

## Solution
#### Python
```python
def caseConversion (s):
    words = []
    word = ""
    for i,j in enumerate(s):
        if i == 0:
            word += j.lower()
        elif j.isupper():
            words.append(word.lower())
            word = j
        else:
            word += j
    words.append(word.lower())
    return "_".join(words)
T = int(input())
for _ in range(T):
    s = input()
    out_ = caseConversion(s)
    print (out_)
```
        