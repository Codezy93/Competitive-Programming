
# Collection Deque

Date: 07-09-2024

## Solution
#### Python
```python
from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input()
    if inp == 'popleft':
        d.popleft()
    elif inp == 'pop':
        d.pop()
    elif 'appendleft' in inp:
        inp = int(inp.split(" ")[1])
        d.appendleft(inp)
    else:
        inp = int(inp.split(" ")[1])
        d.append(inp)
for i in d:
    print(i, end=" ")
```
        