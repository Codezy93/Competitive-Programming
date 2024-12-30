# Notes and Coins

Date: 2024-10-14 10:16:05.314276

## Solution

#### Python
```python
notes = []
print("Coins :")
for _ in range(0, int(input())):
    a, b = input().split(" ")
    if a == "Note":
        notes.append(b)
    else:
        print(b)
print("Notes :")
for i in notes:
    print(i)
 ```