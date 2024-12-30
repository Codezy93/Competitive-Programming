
# Monk and Suffix Sort

Date: 23-08-2024

## Solution
#### Python
```python
string, index = input().split(" ")
suffix = []
for i in range(0, len(string)):
    suffix.append(string[i:])
suffix.sort()
print(suffix[int(index)-1])
```
        