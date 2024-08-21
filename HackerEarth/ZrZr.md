
# ZrZr

Date: 21-08-2024

## Solution
#### Python
```python
for _ in range(0, int(input())):
    n = int(input())
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    print(count)
```
        