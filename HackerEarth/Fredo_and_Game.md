
# Fredo and Game

Date: 12-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    b, l = map(int, input().split(' '))
    arr = [int(x) for x in input().split(' ')]
    index = 1
    for x, i in enumerate(arr):
        if i == 1:
            b += 2
        else:
            b -= 1
        if b == 0 and x != len(arr)-1:
            print(f'No {index}')
            break
        index += 1
    else:
        print(f'Yes {b}')
```
        