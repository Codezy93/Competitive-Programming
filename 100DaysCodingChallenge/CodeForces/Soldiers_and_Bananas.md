
# Soldiers and Bananas

Date: 19-09-2024

## Solution
#### Python
```python
k, n, w = map(int, input().split(" "))
cost = int((w/2)*(1+w)*k)
print(cost-n) if cost>n else print(0)
```
        