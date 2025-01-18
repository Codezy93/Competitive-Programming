# 407. Trapping Rain Water II

---

Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return _the volume of water it can trap after raining_.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg)


**Input:** heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
**Output:** 4
**Explanation:** After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.


**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg)


**Input:** heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
**Output:** 10


 

**Constraints:**

  * `m == heightMap.length`
  * `n == heightMap[i].length`
  * `1 <= m, n <= 200`
  * `0 <= heightMap[i][j] <= 2 * 104`

---

## Solution



---

## Code
```python
from heapq import heappop, heappush 

class Solution:
    def trapRainWater(self, height_map: List[List[int]]) -> int:
        rows, cols = len(height_map), len(height_map[0])
        visited = [[False] * cols for _ in range(rows)]
        min_heap = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (height_map[i][j], i, j))
                    visited[i][j] = True
        trapped_water = 0
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        while min_heap:
            height, x, y = heappop(min_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    trapped_water += max(0, height - height_map[nx][ny])
                    visited[nx][ny] = True
                    heappush(min_heap, (max(height, height_map[nx][ny]), nx, ny))
        return trapped_water
```