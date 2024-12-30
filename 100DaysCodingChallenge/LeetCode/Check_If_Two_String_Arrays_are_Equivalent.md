# Check If Two String Arrays are Equivalent

Date: 2024-10-14 10:16:05.314276

## Solution

#### Python
```python
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)
 ```