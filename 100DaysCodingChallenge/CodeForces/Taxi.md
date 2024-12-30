# Taxi

Date: 2024-10-15 00:00:00

## Solution

#### Python
```python
n = int(input())
groups = list(map(int, input().split()))
count = [0] * 5
for group in groups:
    count[group] += 1
taxis = count[4]
min_pairs = min(count[3], count[1])
taxis += min_pairs
count[3] -= min_pairs
count[1] -= min_pairs
taxis += count[3]
taxis += count[2] // 2
if count[2] % 2:
    taxis += 1
    count[1] -= min(2, count[1])
if count[1] > 0:
    taxis += (count[1] + 3) // 4
print(taxis)
 ```