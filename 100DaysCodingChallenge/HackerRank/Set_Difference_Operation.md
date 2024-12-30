# Set Difference Operation

Date: 2024-11-02 00:00:00

## Solution

#### Python
```python
l1 = int(input())
s1 = set(input().split(" "))
l2 = int(input())
s2 = set(input().split(" "))
print(len(s1.difference(s2)))
 ```