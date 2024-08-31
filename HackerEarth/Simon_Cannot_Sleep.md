
# Simon Cannot Sleep

Date: 31-08-2024

## Solution
#### Python
```python
import math
h, m = map(int, input().split(":"))
total_seconds = h * 3600 + m * 60
d = 3927.272727272727
ans = total_seconds / d + 1
print(math.floor(ans))
```
        