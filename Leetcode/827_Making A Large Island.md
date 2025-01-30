# 827. Making A Large Island

---

You are given an `n x n` binary matrix `grid`. You are allowed to change **at most one ** `0` to be `1`.

Return _the size of the largest **island ** in_ `grid` _after applying this operation_.

An **island ** is a 4-directionally connected group of `1`s.

 

**Example 1:**


**Input:** grid = [[1,0],[0,1]]
**Output:** 3
**Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3.


**Example 2:**


**Input:** grid = [[1,1],[1,0]]
**Output:** 4
**Explanation:** Change the 0 to 1 and make the island bigger, only one island with area = 4.

**Example 3:**


**Input:** grid = [[1,1],[1,1]]
**Output:** 4
**Explanation:** Can't change any 0 to 1, only one island with area = 4.


 

**Constraints:**

  * `n == grid.length`
  * `n == grid[i].length`
  * `1 <= n <= 500`
  * `grid[i][j]` is either `0` or `1`.

---

## Solution



---

## Code
```python
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find_root(element):
            if parents[element] != element:
                parents[element] = find_root(parents[element])
            return parents[element]
        def union_sets(set1, set2):
            root1, root2 = find_root(set1), find_root(set2)
            if root1 == root2:
                return
            parents[root1] = root2
            set_sizes[root2] += set_sizes[root1]
        n = len(grid)
        parents = list(range(n * n))
        set_sizes = [1] * (n * n)
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value:
                    for a, b in [[0, -1], [-1, 0]]:
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n and grid[x][y]:
                            union_sets(x * n + y, i * n + j)
        max_island_size = max(set_sizes)
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 0:
                    visited_roots = set()
                    temp_size = 1
                    for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        x, y = i + a, j + b
                        if 0 <= x < n and 0 <= y < n and grid[x][y]:
                            root = find_root(x * n + y)
                            if root not in visited_roots:
                                visited_roots.add(root)
                                temp_size += set_sizes[root]
                    max_island_size = max(max_island_size, temp_size)
        return max_island_size
```