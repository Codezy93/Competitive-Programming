# Odd Even

Date: 2024-10-07 21:37:19.085381

## Solution

#### Python
```python
n, number = map(int, input().split(" "))
if number <= (n+1)/2:
    print((2*number)-1)
else:
    number = number - ((n+1)//2)
    print(2*number)
 ```