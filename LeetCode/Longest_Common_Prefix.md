
# Longest Common Prefix

Date: 27-08-2024

## Solution
#### Python
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_len = 9999
        for i in strs:
            if len(i) < min_len:
                min_len = len(i)
        for i in range(0, min_len):
            letter = ""
            for j in range(0, len(strs)):
                if j == 0:
                    letter = strs[0][i]
                else:
                    if strs[j][i] != letter:
                        return prefix
            prefix = prefix + letter
        return prefix
```
        