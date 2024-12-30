# Coin Game

Date: 2024-10-09 17:57:48.744318

## Solution

#### Python
```python
def turns(num):
    count = 0
    while num%2==0:
        count += 1
        num /= 2
    return count
for _ in range(0, int(input())):
    length = int(input())
    print('Alan' if sum([turns(int(x)) for x in input().split(" ")])%2==0 else 'Charlie')
 ```