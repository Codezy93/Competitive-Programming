# Truncate Sentence

Date: 2024-10-08 09:11:16.441053

## Solution

#### Python
```python
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[0:k])
 ```