# Add Odd or Subtract Even

Date: 2024-11-10 10:05:23.217940

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
            print(1)
        else:
            print(2)
    elif a < b:
        if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
            print(2)
        else:
            print(1)
    else:
        print(0)
 ```