# Alien Language

Date: 2024-10-20 00:00:00

## Solution

#### Python
```python
n = int(input())
for i in range(n):
    first_word = input()
    second_word = input()
    for i in second_word:
        if i in first_word:
            print("YES")
            break
    else:
        print("NO")
 ```