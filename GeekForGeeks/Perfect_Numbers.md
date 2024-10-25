# Perfect Numbers

Date: 2024-10-25 12:33:26.225139

## Solution

#### Python
```python
class Solution:
    def isPerfectNumber(self, N):
        sum = 0
        if N == 1:
            return 0
        for i in range(1, int(N**0.5)+1):
            if N%i == 0:
                sum += i
                if i != 1:
                    sum += N//i
        if sum == N:
            return 1
        else:
            return 0
 ```