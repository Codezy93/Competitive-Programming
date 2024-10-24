# All Vowels

Date: 2024-10-24 00:00:00

## Solution

#### Python
```python
n = int(input())
string = input()
vowels = ['a', 'e', 'i', 'o', 'u']
for i in string:
    if i in vowels:
        vowels.remove(i)
print('YES' if len(vowels) == 0 else 'NO')
 ```