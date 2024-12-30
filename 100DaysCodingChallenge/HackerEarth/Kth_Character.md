
# Kth Character

Date: 03-09-2024

## Solution
#### Python
```python
string = input()
letters = list(set(list(string)))
substring = []
for i in letters:
    word = ""
    for j in string:
        if i != j:
            word = word + j
    substring.append(word)
substring.sort()
print(substring[0])
```
        