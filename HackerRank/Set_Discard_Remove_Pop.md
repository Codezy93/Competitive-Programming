
# Set Discard Remove Pop

Date: 18-09-2024

## Solution
#### Python
```python
n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    string = input()
    if string == "pop":
        s.pop()
    else:
        string = string.split(" ")
        num = int(string[1])
        string = string[0]
        if string == "remove":
            s.remove(num)
        elif string == "discard":
            s.discard(num)
        else:
            pass
print(sum(s))
```
        