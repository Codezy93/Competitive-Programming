
# Queue at School

Date: 25-09-2024

## Solution
#### Python
```python
def reorder(string):
    string = list(string)
    index = 0
    while index<len(string)-1:
        if string[index] == "B" and string[index+1] == "G":
            string[index] = "G"
            string[index+1] = "B"
            index += 2
        else:
            index += 1
    return "".join(string)
length, iter = map(int, input().split(" "))
string = input()
for _ in range(iter):
    string = reorder(string)
print(string)
```
        