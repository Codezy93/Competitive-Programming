# Capitalize Title

Date: 2024-10-26 18:21:47.060623

## Solution

#### Python
```python
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split(" ")
        for i, j in enumerate(title):
            if len(j) < 3:
                title[i] = j.lower()
            else:
                title[i] = j.capitalize()
        return " ".join(title)
 ```