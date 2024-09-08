
# Shortest Knight Path

Date: 08-09-2024

## Solution
#### Python
```python
from collections import deque
knight_moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]
def algebraic_to_coordinates(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (row, col)
def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8
def knight(start, end):
    start_pos = algebraic_to_coordinates(start)
    end_pos = algebraic_to_coordinates(end)
    if start_pos == end_pos:
        return 0
    queue = deque([(start_pos[0], start_pos[1], 0)])
    visited = set()
    visited.add(start_pos)
    while queue:
        x, y, steps = queue.popleft()
        for dx, dy in knight_moves:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) == end_pos:
                return steps + 1
            if is_valid(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, steps + 1))
    return -1
```
        