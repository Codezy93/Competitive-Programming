
# Prateek and his friends

Date: 30-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    N, X = map(int, input().split(" "))
    arr = []
    for i in range(N):
        arr.append(int(input()))
    state = True
    for i in range(len(arr)):
        sum = arr[i]
        if sum == X:
            print('YES')
            state = False
            break
        for j in range(i+1, len(arr)):
            if sum == X:
                print('YES')
                state = False
                break
            elif sum > X:
                break
            else:
                sum += arr[j]
                if sum == X:
                    print('YES')
                    state = False
                    break
        if not state:
            break
    else:
        if state:
            print('NO')
```
        