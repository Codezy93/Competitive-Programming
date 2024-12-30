# Find difference between sum of diagonals

Date: 05/08/2024

## Solution
#### Python
```python
class Solution:
    def diagonalSumDifference(self,N,Grid):
        s1 = 0
        s2 = 0
        for i in range(0, N):
            s1 += Grid[i][i]
            s2 += Grid[i][N-1-i]
        return abs(s2-s1)

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Grid = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            s=list(map(int,input().strip().split(' ')))
            for j in range(N):
                Grid[i][j]=s[j]
        ob=Solution()
        print(ob.diagonalSumDifference(N,Grid))
```