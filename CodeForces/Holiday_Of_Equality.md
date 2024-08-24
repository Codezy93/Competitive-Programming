
# Holiday Of Equality

Date: 24-08-2024

## Solution
#### Python
```python
length = int(input())
arr = [int(x) for x in input().split(" ")]
max_coin = max(arr)
arr = [max_coin-x for x in arr]
print(sum(arr))
```
        