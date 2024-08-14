
# Chat Room

Date: 14-08-2024

## Solution
#### Python
```python
chat = input()
curr = 0
word = "hello"
for i in chat:
    if i == word[curr]:
        curr += 1
        if curr == 5:
            break
    else:
        pass
if curr == 5:
    print("YES")
else:
    print("NO")
```
        