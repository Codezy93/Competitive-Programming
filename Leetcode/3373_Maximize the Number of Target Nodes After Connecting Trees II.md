# 3373. Maximize the Number of Target Nodes After Connecting Trees II

---

There exist two **undirected ** trees with `n` and `m` nodes, labeled from `[0, n - 1]` and `[0, m - 1]`, respectively.

You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi` in the second tree.

Node `u` is **target ** to node `v` if the number of edges on the path from `u` to `v` is even. **Note ** that a node is _always_ **target ** to itself.

Return an array of `n` integers `answer`, where `answer[i]` is the **maximum ** possible number of nodes that are **target ** to node `i` of the first tree if you had to connect one node from the first tree to another node in the second tree.

**Note ** that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

 

**Example 1:**

**Input:** edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]

**Output:** [8,7,7,8,8]

**Explanation:**

  * For `i = 0`, connect node 0 from the first tree to node 0 from the second tree.
  * For `i = 1`, connect node 1 from the first tree to node 4 from the second tree.
  * For `i = 2`, connect node 2 from the first tree to node 7 from the second tree.
  * For `i = 3`, connect node 3 from the first tree to node 0 from the second tree.
  * For `i = 4`, connect node 4 from the first tree to node 4 from the second tree.

![](https://assets.leetcode.com/uploads/2024/09/24/3982-1.png)

**Example 2:**

**Input:** edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]

**Output:** [3,6,6,6,6]

**Explanation:**

For every `i`, connect node `i` of the first tree with any node of the second tree.

![](https://assets.leetcode.com/uploads/2024/09/24/3928-2.png)

 

**Constraints:**

  * `2 <= n, m <= 105`
  * `edges1.length == n - 1`
  * `edges2.length == m - 1`
  * `edges1[i].length == edges2[i].length == 2`
  * `edges1[i] = [ai, bi]`
  * `0 <= ai, bi < n`
  * `edges2[i] = [ui, vi]`
  * `0 <= ui, vi < m`
  * The input is generated such that `edges1` and `edges2` represent valid trees.

---

## Solution



---

## Code
```python
class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> List[int]:
        def build(edges: List[List[int]]) -> List[List[int]]:
            n = len(edges) + 1
            g = [[] for _ in range(n)]
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            return g
        def dfs(
            g: List[List[int]], a: int, fa: int, c: List[int], d: int, cnt: List[int]
        ):
            c[a] = d
            cnt[d] += 1
            for b in g[a]:
                if b != fa:
                    dfs(g, b, a, c, d ^ 1, cnt)
        g1 = build(edges1)
        g2 = build(edges2)
        n, m = len(g1), len(g2)
        c1 = [0] * n
        c2 = [0] * m
        cnt1 = [0, 0]
        cnt2 = [0, 0]
        dfs(g2, 0, -1, c2, 0, cnt2)
        dfs(g1, 0, -1, c1, 0, cnt1)
        t = max(cnt2)
        return [t + cnt1[c1[i]] for i in range(n)]
```