# Soft Drinking

Date: 2024-10-28 00:00:00

## Solution

#### Python
```python
n, k, l, c, d, p, nl, np = map(int, input().split())
result = min(k * l // nl, c * d, p // np) // n
print(result)
 ```