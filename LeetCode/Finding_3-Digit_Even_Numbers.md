# Finding 3-Digit Even Numbers

Date: 2024-10-19 00:00:00

## Solution

#### Python
```python
class Solution:
  def findEvenNumbers(self, digits: list[int]) -> list[int]:
    ans = []
    count = collections.Counter(digits)
    for a in range(1, 10):
      for b in range(0, 10):
        for c in range(0, 9, 2):
          if count[a] > 0 and count[b] > (
                  b == a) and count[c] > (
                  c == a) + (
                  c == b):
            ans.append(a * 100 + b * 10 + c)
    return ans
 ```