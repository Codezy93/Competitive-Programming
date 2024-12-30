# Max number of baloons

Date: 2024-10-12 18:03:23.457274

## Solution

#### Python
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = text.lower()
        ideal = {'b':1, 'a':1, "l":2, "o":2, 'n':1}
        map = {}
        min = 99999
        for i in text:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        for i in 'balon':
            if i not in map:
                return 0
            temp = map[i]//ideal[i]
            if min > temp:
                min = temp
        return min
 ```