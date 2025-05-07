# 3341. Find Minimum Time to Reach Last Room I

---

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum ** time in seconds when you can **start moving ** to that room. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent ** room. Moving between adjacent rooms takes _exactly_ one second.

Return the **minimum ** time to reach the room `(n - 1, m - 1)`.

Two rooms are **adjacent ** if they share a common wall, either _horizontally_ or _vertically_.

 

**Example 1:**

**Input:** moveTime = [[0,4],[4,4]]

**Output:** 6

**Explanation:**

The minimum time required is 6 seconds.

  * At time `t == 4`, move from room `(0, 0)` to room `(1, 0)` in one second.
  * At time `t == 5`, move from room `(1, 0)` to room `(1, 1)` in one second.



**Example 2:**

**Input:** moveTime = [[0,0,0],[0,0,0]]

**Output:** 3

**Explanation:**

The minimum time required is 3 seconds.

  * At time `t == 0`, move from room `(0, 0)` to room `(1, 0)` in one second.
  * At time `t == 1`, move from room `(1, 0)` to room `(1, 1)` in one second.
  * At time `t == 2`, move from room `(1, 1)` to room `(1, 2)` in one second.



**Example 3:**

**Input:** moveTime = [[0,1],[1,2]]

**Output:** 3

 

**Constraints:**

  * `2 <= n == moveTime.length <= 50`
  * `2 <= m == moveTime[i].length <= 50`
  * `0 <= moveTime[i][j] <= 109`

---

## Solution



---

## Code
```python
class Solution:
  def minTimeToReach(self, moveTime: list[list[int]]) -> int:
    return self._dijkstra(moveTime, (0, 0), (len(moveTime) - 1, len(moveTime[0]) - 1))
  def _dijkstra(self, moveTime: list[list[int]], src: tuple[int, int], dst: tuple[int, int]) -> int:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    m = len(moveTime)
    n = len(moveTime[0])
    dist = [[math.inf] * n for _ in range(m)]
    dist[0][0] = 0
    minHeap = [(0, src)]
    while minHeap:
      d, u = heapq.heappop(minHeap)
      if u == dst:
        return d
      i, j = u
      if d > dist[i][j]:
        continue
      for dx, dy in DIRS:
        x = i + dx
        y = j + dy
        if x < 0 or x == m or y < 0 or y == n:
          continue
        newDist = max(moveTime[x][y], d) + 1
        if newDist < dist[x][y]:
          dist[x][y] = newDist
          heapq.heappush(minHeap, (newDist, (x, y)))
    return -1
```