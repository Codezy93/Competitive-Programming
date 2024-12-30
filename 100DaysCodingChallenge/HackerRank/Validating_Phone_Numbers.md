
# Validating Phone Numbers

Date: 11-08-2024

## Solution
#### Python
```python
for _ in range(int(input())):
    number = input()
    valid = ["7", "8", "9"]
    if len(number) == 10 and number[0] in valid:
        try:
            int(number)
            print("YES")
        except:
            print("NO")
    else:
        print("NO")
```
        