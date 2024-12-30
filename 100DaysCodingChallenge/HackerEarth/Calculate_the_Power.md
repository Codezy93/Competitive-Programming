
# Calculate the Power

Date: 16-08-2024

## Solution
#### Python
```python
x, y = map(int, input().split())
result = 1
mod = (10**9)+7
x = x % mod
while y > 0:
    if y % 2 == 1:
        result = (result * x) % mod
    y = y // 2 
    x = (x * x) % mod
print(result)
```
        