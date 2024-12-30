# Balanced Arrays

Date: 2024-11-05 00:00:00

## Solution

#### Python
```python
t = int(input())
for _ in range(t):
    n = int(input())
    if (n // 2) % 2 != 0:
        print("NO")
        continue
    else:
        print("YES")
        even_half = [2 * i for i in range(1, n // 2 + 1)]
        odd_half = [2 * i - 1 for i in range(1, n // 2)]
        print(" ".join(map(str, even_half)), end=" ")
        print(" ".join(map(str, odd_half)), end=" ")
        print(n // 2 + n - 1)
 ```