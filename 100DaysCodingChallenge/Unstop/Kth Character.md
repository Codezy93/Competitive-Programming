# Kth Character

Date: 05/08/2024

## Solution
#### Python
```python
n, k = [int(x) for x in input().split(" ")]
letters = input()
letters = letters[::-1]
print(letters[k-1])
```