
# Excursion

Date: 01-09-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    N, M, K = map(int, input().split(" "))
    rooms = (M + K - 1) // K + (N + K - 1) // K
    print(rooms)
```
        