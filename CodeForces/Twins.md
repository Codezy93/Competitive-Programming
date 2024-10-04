# Twins

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
arr.sort(reverse=True)
total = sum(arr)
temp = 0
coins = 0
for i in arr:
    coins += 1
    temp += i
    if temp > total-temp:
        print(coins)
        break
 ```