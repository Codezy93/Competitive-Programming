# Favourite Singer


Date: 06/08/2024

## Solution
#### Python
```python
from collections import Counter

# Read input
length = int(input())
play = input().split()

# Count occurrences of each item
play_count = Counter(play)

# Find the maximum count
max_count = max(play_count.values())

# Count how many items have the maximum count
most_common_count = sum(1 for count in play_count.values() if count == max_count)

# Output the result
print(most_common_count)
```