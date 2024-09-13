
# String Sum

Date: 13-09-2024

## Solution
#### Python
```python
weights = {}
letters = "abcdefghijklmnopqrstuvwxyz"
for i, j in enumerate(letters):
    weights[j] = i+1
string = input()
sum = 0
for i in string:
    sum += weights[i]
print(sum)
```
        