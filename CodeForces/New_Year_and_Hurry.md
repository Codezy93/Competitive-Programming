# New Year and Hurry

Date: 2024-11-08 00:00:00

## Solution

#### Python
```python
n, k = map(int, input().split(" "))
sum_ = 0
i = 1
while i <= n:
    if sum_ + (5 * i) > (240 - k):
        break
    sum_ += (5 * i)
    i += 1
i -= 1
print(i)
 ```