
# String Task

Date: 17-09-2024

## Solution
#### Python
```python
string = input().lower()
vowels = "aeiouy"
for i in vowels:
    string = string.replace(i, "")
res = ""
for i in string:
    res = res + "." + i
print(res)
```
        