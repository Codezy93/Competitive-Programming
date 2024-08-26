
# Keyboard Row

Date: 26-08-2024

## Solution
#### Python
```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        out = []
        for w in words:
            i = w.lower()
            for r in rows:
                if i[0] in r:
                    for j in i:
                        if j not in r:
                            break
                    else:
                        out.append(w)
        return out
```
        