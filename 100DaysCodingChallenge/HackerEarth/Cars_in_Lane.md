# Cars in Lane

Date: 2024-10-04 00:00:00

## Solution

#### Python
```python
for _ in range(int(input())):
    print(2**list(bin(int(input()))).count("1"))
 ```