# Watermelon

Date: 05/08/2024

## Solution
#### Python
```python
w = int(input())

if w % 2 != 0 or w == 2:
    print("NO")
else:
    for w1 in range(2, w+1, 2):
        print(w1)
        if w1%2==0 and (w-w1)%2 == 0:
            print('YES')
            break
    else:
        print("NO")
```