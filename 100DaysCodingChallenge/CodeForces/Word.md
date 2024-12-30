# Word

Date: 07-08-2024

## Solution
#### Python
```python
string = input()
low = 0
up = 0
for i in string:
    if i.islower():
        low += 1
    else:
        up += 1
if low >= up:
    print(string.lower())
else:
    print(string.upper())
```