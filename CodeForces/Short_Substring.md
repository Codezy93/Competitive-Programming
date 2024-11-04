# Short Substring

Date: 2024-11-04 00:00:00

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    s = input()
    print(s[0], end="")
    for i in range(1, len(s), 2):
        print(s[i], end="")
    print()
 ```