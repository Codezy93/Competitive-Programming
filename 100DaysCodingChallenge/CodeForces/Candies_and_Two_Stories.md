# Candies and Two Stories

Date: 2024-10-18 00:00:00

## Solution

#### Python
```python
for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print(n // 2 + 1)
    else:
        print(n // 2)
 ```