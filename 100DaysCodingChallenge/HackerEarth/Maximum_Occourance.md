# Maximum Occourance

Date: 2024-10-25 12:33:26.225139

## Solution

#### Python
```python
map = {}
string = input()
for i in string:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1
max = 0
max_char = 0
for i in map:
    if map[i] > max:
        max = map[i]
        max_char = i
    elif map[i] == max:
        if i < max_char:
            max_char = i
    else:
        pass
print(max_char, max)
 ```