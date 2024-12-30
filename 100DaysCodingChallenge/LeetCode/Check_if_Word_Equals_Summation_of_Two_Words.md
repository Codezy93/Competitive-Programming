# Check if Word Equals Summation of Two Words

Date: 2024-10-30 00:00:00

## Solution

#### Python
```python
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def decode(string):
            map  = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
            out = ""
            for i in string:
                out = out + str(map[i])
            return int(out)
        return decode(firstWord)+decode(secondWord) == decode(targetWord)
 ```