
# Anton and Danik

Date: 11-09-2024

## Solution
#### Python
```python
length = input()
string = input()
a = string.count('A')
d = string.count('D')
if a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')
```
        