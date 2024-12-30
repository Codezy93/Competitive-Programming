
# Bit++

Date: 31-08-2024

## Solution
#### Python
```python
def print_increment(X):
    X += 1
    return X
def increment_print(X):
    X += 1
    return X
def print_decrement(X):
    X -= 1
    return X  
def decrement_print(X):
    X -= 1
    return X
X = 0
for i in range(int(input())):
    inp = input()
    if inp == "++X":
        X = increment_print(X)
    elif inp == "X++":
        X = print_increment(X)
    elif inp == "--X":
        X = decrement_print(X)
    elif inp == "X--":
        X = print_decrement(X)
    else:
        pass
print(X)
```
        