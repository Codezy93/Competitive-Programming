# 1931. Painting a Grid With Three Different Colors

---

You are given two integers `m` and `n`. Consider an `m x n` grid where each cell is initially white. You can paint each cell **red ** , **green ** , or **blue **. All cells **must ** be painted.

Return _the number of ways to color the grid with **no two adjacent cells having the same color **_. Since the answer can be very large, return it **modulo ** `109 + 7`.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png)


**Input:** m = 1, n = 1
**Output:** 3
**Explanation:** The three possible colorings are shown in the image above.


**Example 2:**

![](https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png)


**Input:** m = 1, n = 2
**Output:** 6
**Explanation:** The six possible colorings are shown in the image above.


**Example 3:**


**Input:** m = 5, n = 5
**Output:** 580986


 

**Constraints:**

  * `1 <= m <= 5`
  * `1 <= n <= 1000`

---

## Solution



---

## Code
```python
from collections import defaultdict

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def is_valid_pattern(pattern: int) -> bool:
            last_color = -1
            for _ in range(m):
                current_color = pattern % 3
                if current_color == last_color:
                    return False
                last_color = current_color
                pattern //= 3
            return True
        def are_adjacent_patterns_valid(first: int, second: int) -> bool:
            for _ in range(m):
                if first % 3 == second % 3:
                    return False
                first, second = first // 3, second // 3
            return True
        mod = 10**9 + 7
        max_pattern_value = 3**m
        valid_patterns = {i for i in range(max_pattern_value) if is_valid_pattern(i)}
        adjacent_patterns = defaultdict(list)
        for pattern in valid_patterns:
            for adjacent in valid_patterns:
                if are_adjacent_patterns_valid(pattern, adjacent):
                    adjacent_patterns[pattern].append(adjacent)
        ways_to_color = [int(pattern in valid_patterns) for pattern in range(max_pattern_value)]
        for _ in range(n - 1):
            next_column_ways = [0] * max_pattern_value
            for pattern in valid_patterns:
                for adjacent in adjacent_patterns[pattern]:
                    next_column_ways[pattern] = (next_column_ways[pattern] + ways_to_color[adjacent]) % mod
            ways_to_color = next_column_ways
        return sum(ways_to_color) % mod
```