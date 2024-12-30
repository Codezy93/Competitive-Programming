
# Shil and Palindrome

Date: 29-09-2024

## Solution
#### Python
```python
string = input()
map = {}
for i in string:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1
odd = 0
oddl = ""
for i in map:
    if map[i]%2 != 0:
        odd += 1
        oddl = i
        map[i] -= 1
if odd > 1:
    print(-1)
else:
    letters = [x*(map[x]//2) for x in map]
    letters = "".join(sorted(letters))
    print(letters+oddl+letters[::-1])
```
        