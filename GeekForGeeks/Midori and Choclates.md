# Midori and Choclates

Platform: GeeksforGeeks

Date: 06/08/2024

## Problem
Midori like chocolates and he loves to try different ones. There are N shops in a market labelled from 1 to N and each shop offers a different variety of chocolate. Midori starts from ith shop and goes ahead to each and every shop. But as there are too many shops Midori would like to know how many more shops he has to visit. You have been given L denoting number of bits required to represent N. You need to return the maximum number of shops he can visit.

## Input
Two integers i and L, i denoting current shop index and L denoting number of bits in N.

## Output
Integer denoting number of shops remaining

## Solution
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