# Midori and Choclates

Date: 06/08/2024

## Solution
#### Python
```python
class Solution:
    def leftShops (self, i, L):
        return (2**L)-i
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        i, L = input().split()
        i = int(i)
        L = int(L)
        ob = Solution()
        print(ob.leftShops(i, L))
```