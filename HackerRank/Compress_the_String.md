
# Compress the String

Date: 01-09-2024

## Solution
#### Python
```python
string = input()
curr = string[0]
count = 1
for i, j in enumerate(string):
    if i == 0:
        pass
    else:
        if j == curr:
            count += 1
        else:
            print((count, int(curr)), end=" ")
            curr = j
            count = 1
print((count, int(curr)), end=" ")
```
        