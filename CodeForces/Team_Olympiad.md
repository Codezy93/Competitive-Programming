# Team Olympiad

Date: 2024-11-03 00:00:00

## Solution

#### Python
```python
n = int(input())
arr = list(map(int, input().split()))
one, two, three = [], [], []
count1 = count2 = count3 = 0
for i in range(n):
    if arr[i] == 1:
        one.append(i + 1)
        count1 += 1
    elif arr[i] == 2:
        two.append(i + 1)
        count2 += 1
    else:
        three.append(i + 1)
        count3 += 1
min_count = min(count1, count2, count3)
print(min_count)
for i in range(min_count):
    print(one[i], two[i], three[i])
 ```