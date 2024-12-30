
# Bear and Big Brother

Date: 11-08-2024

## Solution
#### Python
```python
a, b = [int(x) for x in input().split(" ")]
count = 0
while b >= a:
    a *= 3
    b *= 2
    count += 1
print(count)
```
        