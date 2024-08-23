
# Collections Counter

Date: 23-08-2024

## Solution
#### Python
```python
from collections import Counter
length = int(input())
inventory = [int(x) for x in input().split(" ")]
inventory = Counter(inventory)
total = 0
for  _ in range(int(input())):
    size, price = [int(x) for x in input().split(" ")]
    if size in inventory and inventory[size] != 0:
        total += price
        inventory[size] -= 1
print(total)
```
        