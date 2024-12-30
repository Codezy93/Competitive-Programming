# Stack and Queues

Date: 2024-10-22 00:00:00

## Solution

#### Python
```python
n , k = map(int,input().split())
l = list(map(int,input().split()))
s = 0
for i in range(k):
    s += l[i]
m = s
for i in range(k-1):
    s = s - l[k-i-1] + l[n-1-i]
    if s>=m:
        m=s
print(m)
 ```