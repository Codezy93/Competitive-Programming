
# Stones on the Table

Date: 18-09-2024

## Solution
#### Python
```python
length = input()
stones = list(input())
index = 0
count = 0
while index < len(stones)-1:
    if stones[index] == stones[index+1]:
        del stones[index]
        count += 1
    else:
        index += 1
print(count)
```
        