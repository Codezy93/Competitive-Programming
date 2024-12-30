
# Illegible String

Date: 06-09-2024

## Solution
#### Python
```python
length = int(input())
string = input()
string = string.replace("w", "vv")
max_len = len(string)
string = string.replace("vv", "w")
min_len = len(string)
print(min_len, max_len)
```
        