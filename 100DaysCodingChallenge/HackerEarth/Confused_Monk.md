# Confused Monk

Date: 2024-10-28 00:00:00

## Solution

#### Python
```python
def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_of_array(arr):
    gcd = arr[0]
    for num in arr[1:]:
        gcd = compute_gcd(gcd, num)
    return gcd
length = int(input())
arr = list(map(int, input().split(" ")))
prod = 1
for i in arr:
    prod *= i
arr.sort()
gcd = gcd_of_array(arr)
print((prod**gcd)%1000000007)
 ```