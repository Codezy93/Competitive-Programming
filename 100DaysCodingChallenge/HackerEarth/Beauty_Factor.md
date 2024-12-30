
# Beauty Factor

Date: 17-09-2024

## Solution
#### Python
```python
def factor(num):
    while num > 9:
        temp = 0
        for i in str(num):
            temp += int(i)
        num = temp
    return num
N, M = map(int, input().split(' '))
if M == 9:
    print(-1)
else:
    for i in range(10**(M-1), 10**M):
        if '0' in str(i):
            pass
        elif len(set(list(str(i)))) != len(str(i)):
            pass
        elif factor(i) == N:
            print(i)
            break
        else:
            pass
    else:
        print(-1)
```
        